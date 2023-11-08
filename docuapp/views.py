from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import DocPost, Profile
from django.contrib.auth.mixins import LoginRequiredMixin

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
    queryset = DocPost.objects.filter(status=1).order_by('-created_on')
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












    
