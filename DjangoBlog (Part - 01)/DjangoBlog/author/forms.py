from django import forms
from . import models


class AuthorForm(forms.ModelForm):

    class Meta:
        model = models.Author
        fields = "__all__"
        labels = {
            "name": "Author's Name",
            "bio": "Author's Bio",
            "phone_no": "Author's Phone Number",
        }
        help_texts = {
            "name": "Enter Full Name",
            "bio": "Write a Short Introduction about youself",
            "phone_no": "Enter the Mobile Number",
        }
        error_messages = {
            "name": {"required": "Name cannot be empty!"},
            "bio": {"required": "A short description is mandatory!"},
            "phone_no": {"required": "A phone number is mandatory to register!"},
        }
