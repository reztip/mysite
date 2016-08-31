from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'body', 'publish_date']

class PostSearchForm(forms.Form):
    post_title = forms.CharField(label = 'Title ', max_length = 70)
    post_body = forms.CharField(label = 'Body ', max_length = 70)

