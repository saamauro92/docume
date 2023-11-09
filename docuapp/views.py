from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from .models import DocPost, Profile, User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfilePicForm

class Home(generic.ListView): 
    """
    Creates home page view with docposts
    """

    model = DocPost
    queryset = DocPost.objects.filter(status=1).order_by('-created_on')
    template_name ='index.html'
    paginate_by = 3

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
                "liked": liked
            },
        )


class ProfileView(LoginRequiredMixin, View): 
    """
    Creates class that returns profile information
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
        


class DeleteDocPost(LoginRequiredMixin, generic.DeleteView):
    """
    User authenticated can delete DocPost from their profile
    Super() will give access to methods and properties of a the class parent
    """
    model = DocPost
    success_url = reverse_lazy('view_profile')

    def delete(self, request, *args, **kwargs):
        return super(DeleteDocPost, self).delete(request, *args, kwargs)
    



class UpdateProfile(LoginRequiredMixin, generic.UpdateView):
    """
    Authenticated user can update profile information
    """
    model = Profile
    form_class = ProfilePicForm
    template_name = 'account/update_profile.html'
    success_url = reverse_lazy('view_profile')


    def form_invalid(self, form):
           form.instance.user = self.request.user
           return super().form_valid(form)
    
    def get_object(self, queryset=None):
          return self.request.user.profile





  
            


        












    
