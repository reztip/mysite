import django.forms

from .models import Post

class PostForm(django.forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'body', 'publish_date']
