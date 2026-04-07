from django import forms
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = "__all__"
        labels = {
            "name": "Student Name",
            "roll": "Student Roll No",
            "fathers_name": "Fathers Name",
            "standard": "Reads in (Class)",
        }
        help_texts = {"name": "Write Your full name"}
        error_messages = {
            "name": {'required' : "Your name is required !!"} 
        }
