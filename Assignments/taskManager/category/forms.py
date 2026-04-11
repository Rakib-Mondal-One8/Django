from django import forms

from category.models import Category


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		labels = {
			'name':"Name",
			'task':'Task'
		}
		help_texts = {
			'name': "Enter the Name of the Category",
			'task': "Enter the Task"
		}
		error_messages = {
			'name': {
				'required': "Please enter the name of the Category"
			},
			'task': {
				'required': "Please enter the name of the Task"
			}
		}