from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Profile

class ProfilePicForm(forms.ModelForm):
    image = forms.ImageField(label="Profile Picture")
    bio = forms.CharField(widget=SummernoteWidget(), label="Biography")
    class Meta:
        model = Profile
        fields = ('image', 'bio')





