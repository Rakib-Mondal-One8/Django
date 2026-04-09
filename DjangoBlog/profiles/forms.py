from django import forms
from . import models


class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = "__all__"
        labels = {"name": "Author's Name", "About": "Description About the Author"}
        help_texts = {"name": "Author's Name", "About": "Description About the Author"}
        error_messages = {
            "name": {"required": "Author's Name is required !"},
            "About": {"required": "You must provide some information !"}
        }
