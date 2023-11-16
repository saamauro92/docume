from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Profile, DocPost, Comment

class ProfilePicForm(forms.ModelForm):
    image = forms.ImageField(label="Profile Picture", required=False)
    bio = forms.CharField(widget=SummernoteWidget(), label="Biography", required=False)
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}),required=False )
    title = forms.CharField(label="Profession" ,required=False)
    name = forms.CharField(label="Name", required=False)
    email = forms.EmailField(label="Email", required=False)

    class Meta:
        model = Profile
        fields = ('name', 'email', 'birth_date', 'title', 'image', 'bio', )

class DocPostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = DocPost
        fields = ('title', 'excerpt', 'featured_image', 'content', 'status','public')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )



