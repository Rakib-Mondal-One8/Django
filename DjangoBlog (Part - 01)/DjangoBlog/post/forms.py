from django import forms
from . import models


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = "__all__"
        labels = {
            "title": "Brief & Descriptive Title",
            "author": "Author's Name",
            "category": "category type",
            "image": "Image Link",
            "content": "Content",
        }
        help_texts = {
            "title": "Give a short and Descriptive title",
            "author": "Give a registered author name",
            "category": "Give a registered category type",
            "image": "Give Image Link",
            "content": "Write your Content",
        }
        error_messages = {
            "title": {"required": "you must provide a title!"},
            "author": {"required": "you must provide a author!"},
            "category": {"required": "you must provide a category!"},
            "image": {"required": "you must provide an image link!"},
            "content": {"required": "you must write some content!"},
        }
