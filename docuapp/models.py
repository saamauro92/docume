from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

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
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    program = models.CharField(max_length=255, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='doc_post_likes', blank=True)
    public = models.BooleanField()

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


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
    
class Profile(models.Model):
    """
    Define profile model that extends the user add user bio, birth_date, image, and title
    https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    title =  models.CharField(max_length=20, blank=True)
    favourites = models.ManyToManyField(DocPost, related_name='favorited_by', blank=True)

    def add_to_favorites(self, docpost):
        if docpost.public:
            self.favourites.add(docpost)

    def remove_from_favorites(self, docpost):
        self.favourites.remove(docpost)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Will create an user profile everytime an user is created
        """
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        Will save the user profile created 
        """
        instance.profile.save()

        def __str__(self):
            return self.user.username
    


    


