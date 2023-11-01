from django.contrib import admin
from .models import DocPost, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(DocPost)

class DocPostAdmin(SummernoteModelAdmin):
    """
    Defines the summernote field content in DocPost for the admin management
    """
    list_display = ('title', 'slug', 'status', 'created_on', 'public')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug' : ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')



@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    """
    Defines admin for comments
    """
    list_display = ('name', 'body', 'docpost', 'created_on')
    list_filter = ('email', 'name', 'created_on')
    search_fields = ('name', 'email', 'body')





