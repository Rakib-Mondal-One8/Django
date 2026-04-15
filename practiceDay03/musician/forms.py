from django import forms

from musician.models import Musician


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_no': 'Phone Number',
            'instrument_type': 'Instrument Type'
        }
        help_texts = {
            'first_name': 'Enter the first name of the musician',
            'last_name': 'Enter the last name of the musician',
            'email': 'Enter the email address of the musician',
            'phone_no': 'Enter the phone number of the musician',
            'instrument_type': 'Enter the instrument type of the musician'
        }
        error_messages = {
            'first_name': {
                'required': 'Please enter your first name',
            },
            'last_name': {
                'required': 'Please enter your last name',
            },
            'email': {
                'required': 'Please enter your email address',
            },
            'phone_no': {
                'required': 'Please enter your phone number',
            },
            'instrument_type': {
                'required': 'Please enter your instrument type',
            }
        }