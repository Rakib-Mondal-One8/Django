from django import forms
from . import models
class CategoryForm(forms.ModelForm): 
    class Meta:
        model = models.Category
        fields = '__all__'
        labels = {
            'name':'Category Name'
        },
        help_texts = {
            'name' : 'Enter Category Name'
        }
        error_messages = {
            'name': {
                'required' : "Empty Category cannot be submitted !"
            }
        }
