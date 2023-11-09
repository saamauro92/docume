from django import forms
from .models import Profile

class ProfilePicForm(forms.ModelForm):
    image = forms.ImageField(label="Profile Picture")
    class Meta:
        model = Profile
        fields = ('image', )





