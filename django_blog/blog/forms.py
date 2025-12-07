from django import forms
from .models import Post
from .widgets import TagWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email') 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget()
        }
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}))

    class Meta:
        model = Comment
        fields = ['content']