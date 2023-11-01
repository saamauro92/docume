from django.contrib import admin
from .models import DocPost
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(DocPost)

class DocPostAdmin(SummernoteModelAdmin):
    """
    Defines the summernote field content in DocPost for the admin management
    """
    summernote_fields = ('content')

