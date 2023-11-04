from django.shortcuts import render
from django.views import generic
from .models import DocPost

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
