from django import forms
from blogapp.models import Blog, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        