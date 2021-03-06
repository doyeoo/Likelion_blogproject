from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'contents']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['author_name', 'comment_text'] 