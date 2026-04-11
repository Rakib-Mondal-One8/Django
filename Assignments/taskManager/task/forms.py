from django import forms

from task.models import Task


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = '__all__'
		labels = {
			'title':"Title",
			'description':"Description",
			'is_done':"Is Done?",
			'assigned_date':"Assigned Date",
		}
		widgets = {
			'assigned_date':forms.DateInput(attrs={'type':'date'}),
		}
		help_texts = {
			'title': "Enter the title",
			'description': "Enter the description",
			'is_done': "Is the task done?",
			'assigned_date': "Date of assigned",
		}
		error_messages = {
			'title': {
				'required': "Title is required",
			},
			'description': {
				'required': "Description is required",
			},
			'is_done': {
				'required': "Is the task done?",
			},
			'assigned_date': {
				'required': "Date of assigned",
			}
		}