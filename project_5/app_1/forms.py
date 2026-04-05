from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField(label="User Name")
    file = forms.FileField()
    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput)

    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    appointment = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    check = forms.BooleanField()

    options_size = [("S", "Small"), ("M", "Medium"), ("L", "Large")]
    size = forms.ChoiceField(choices=options_size, widget=forms.RadioSelect)

    options_pizza = [("P", "Peperoni"), ("C", "Chicken"), ("B", "Beef")]
    pizza = forms.MultipleChoiceField(
        choices=options_pizza, widget=forms.CheckboxSelectMultiple
    )


# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     val_name = self.cleaned_data['name']
#     #     if(len(val_name) < 10):
#     #         raise forms.ValidationError('Name must be atleast of 10 Characters')
#     #     return val_name

#     # def clean_email(self):
#     #     val_email = self.cleaned_data['email']
#     #     if('.com' not in val_email):
#     #         raise forms.ValidationError('Email Should Contain .com')
#     #     return val_email

#     def clean(self):
#         cleaned_data = super().clean() # Default Validation

#         # My own Validation
#         val_name = cleaned_data.get('name')
#         val_email = cleaned_data.get('email')
#         if(len(val_name) < 10):
#             raise forms.ValidationError('Name must be atleast of 10 Characters')
#         if('.com' not in val_email):
#             raise forms.ValidationError('Email Should Contain .com')

#         # Always return cleaned_data
#         return cleaned_data


class StudentForm(forms.Form):
    name = forms.CharField(
        validators=[
            validators.MinLengthValidator(
                10, message="Min Length Should be at least 10"
            ),
        ]
    )
    email = forms.CharField(
        validators=[
            validators.RegexValidator(
                regex="^[a-z0-9@.]+$", message="Format of the email is not currect !!"
            ),
            validators.EmailValidator(message="Give a valid email !"),
        ]
    )
    age = forms.IntegerField(
        validators=[
            validators.MinValueValidator(18, message="Minimum age should be 18 !!"),
            validators.MaxValueValidator(
                100,
                message="Your day is close. Don't waste your time on these sort of things !",
            ),
        ]
    )
    file = forms.FileField(
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=["pdf"], message="File format is not compatible!"
            ),
        ]
    )


class PasswordValidation(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput,
        validators=[
            validators.MinLengthValidator(
                10, message="Name should be atleast 10 character long !"
            ),
        ],
    )
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords Didn't matched !!")
