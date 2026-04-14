from django import forms
from . import models


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = "__all__"
        exclude = ['author']
        labels = {
            "title": "Brief & Descriptive Title",
            "category": "category type",
            "image": "Image Link",
            "content": "Content",
        }
        help_texts = {
            "title": "Give a short and Descriptive title",
            "category": "Give a registered category type",
            "image": "Give Image Link",
            "content": "Write your Content",
        }
        error_messages = {
            "title": {"required": "you must provide a title!"},
            "category": {"required": "you must provide a category!"},
            "image": {"required": "you must provide an image link!"},
            "content": {"required": "you must write some content!"},
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = models.Comment
        exclude = ['post']
        labels = {
            'name' : 'Name',
            'email':'Email',
            'comment': 'Comment'
        }