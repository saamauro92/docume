from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class DocPost(models.Model):
    """
    Defines model for documentation post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doc_post")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='doc_post_likes', blank=True)
    public = models.BooleanField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
    

class Comment(models.Model):
    """
    Defines model for comments on documentation posts
    """
    docpost = models.ForeignKey(DocPost, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    

    


