from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from .models import DocPost, Profile, User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfilePicForm, DocPostForm, CommentForm

class Home(generic.ListView): 
    """
    Creates home page view with docposts
    """
    model = DocPost
    queryset = DocPost.objects.filter(status=1).order_by('-created_on')
    template_name ='index.html'
    paginate_by = 2

class DocPostList(generic.ListView):
    """
    Creates explore page view with docposts
    """
    model = DocPost
    queryset = DocPost.objects.filter(status=1, public=True).order_by('-created_on')
    template_name = 'explore.html'
    paginate_by = 6

class DocPostDetail(View):
    """
    Will use get method to view Docpost details
    
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = DocPost.objects.filter(status=1)
        docpost = get_object_or_404(queryset, slug=slug)
        comments = docpost.comment.order_by('created_on')
        liked = False
        if docpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "docpost_detail.html",
            {
                "docpost": docpost,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = DocPost.objects.filter(status=1)
        docpost = get_object_or_404(queryset, slug=slug)
        comments = docpost.comment.order_by('created_on')
        liked = False
        if docpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment.docpost = docpost
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "docpost_detail.html",
            {
                "docpost": docpost,
                "comments": comments,
                "liked": liked,
                "comment_form": comment_form,
            },
        )

class DeleteDocPost(LoginRequiredMixin, generic.DeleteView):
    """
    User authenticated can delete DocPost from their profile
    Super() will give access to methods and properties of a the class parent
    """
    model = DocPost
    success_url = reverse_lazy('docs')

    def delete(self, request, *args, **kwargs):
        return super(DeleteDocPost, self).delete(request, *args, kwargs)
    


class ProfileView(LoginRequiredMixin, View): 
    """
    Class that returns profile information
    """
    def get(self, request,  *args, **kwargs):
        current_user = request.user
        if current_user.is_authenticated:
             queryset = Profile.objects.filter(user=request.user)
             profile = get_object_or_404(queryset)
             posts = DocPost.objects.filter(author=request.user)
  

             return render(request,
                           'account/profile.html',
                       {  
                             "profile": profile,
                              "docposts": posts,
                          
                             }
                           )
        
class ProfileDocsView(LoginRequiredMixin, View): 
    """
    Class that returns docs information
    """
    def get(self, request,  *args, **kwargs):
        current_user = request.user
        if current_user.is_authenticated:
             queryset = Profile.objects.filter(user=request.user)
             posts = DocPost.objects.filter(author=request.user)
  

             return render(request,
                           'account/docs.html',
                       {  
                              "docposts": posts,
                          
                             }
                           )
        

        
class CreateDocPost(LoginRequiredMixin,generic.CreateView):
    """
    Authenticated user can create a documentation post
    """
    model = DocPost
    form_class = DocPostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('docs')  

    def get_object(self, queryset=None):
      return self.request.user
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            form.instance.program = 'field not used'
            return super(CreateDocPost, self).form_valid(form)
        else:
            return render(self.request, 'account/login.html')

class UpdateDocPost(LoginRequiredMixin, generic.UpdateView):
    """
    Authenticated user can update a documentation post
    """
    model = DocPost
    form_class = DocPostForm
    template_name = 'update_docpost.html'
    success_url = reverse_lazy('docs')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.object = self.get_object()
            form = self.get_form()
            return self.render_to_response(self.get_context_data(form=form, object=self.object))
        else:
            return render(self.request, 'account/login.html')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super(UpdateDocPost, self).form_valid(form)
        else:
            return render(self.request, 'account/login.html')

class UpdateProfile(LoginRequiredMixin, generic.UpdateView):
    """
    Authenticated user can update profile information
    """
    model = Profile
    form_class = ProfilePicForm
    template_name = 'account/update_profile.html'
    success_url = reverse_lazy('view_profile')

    def get_object(self, queryset=None):
        return self.request.user.profile
    
    def get(self, request, *args, **kwargs):
            if self.request.user.is_authenticated:
                self.object = self.get_object()
                form = self.get_form()
                return self.render_to_response(self.get_context_data(form=form, object=self.object))
            else:
                return render(self.request, 'account/login.html')

    def form_invalid(self, form):
           form.instance.user = self.request.user
           return super().form_valid(form)
    
class AddToFavoritesView(LoginRequiredMixin, generic.View):
    """
    Authenticated user will be able to add public docposts to favourites
    """
    def get(self, request, docpost_id):
        docpost = get_object_or_404(DocPost, pk=docpost_id)

        if request.user.is_authenticated:
             if docpost.public and docpost.author != request.user:
               profile = Profile.objects.filter(user=request.user).first()
               if profile is not None:
                    profile.add_to_favorites(docpost)

        return redirect('favourites')

class RemoveFromFavoritesView(LoginRequiredMixin, generic.View):
    """
    Authenticated user will be able to remove a docpost from favourites
    """
    def get(self, request, docpost_id):
        docpost = get_object_or_404(DocPost, pk=docpost_id)

        if request.user.is_authenticated:
            profile = Profile.objects.filter(user=request.user).first()
            if profile is not None:
                profile.remove_from_favorites(docpost)

        return redirect('favourites')

class ProfileFavouritesView(LoginRequiredMixin, generic.ListView):
    """
    Explore list of favourites
    """
    model = Profile
    template_name = 'account/favourites.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_authenticated:
            profile = get_object_or_404(Profile, user=current_user)
            return profile.favourites.all()
        return []



  
            


        












    
