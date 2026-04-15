from django import forms

from album.models import Album
# Album Name
# One-to-Many Relationships with musician model
# Album release date
# Rating between 1-5

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_date' : forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name' : 'Name',
            'musician' : 'Musician',
            'release_date' : 'Released On',
            'rating' : 'Rating',
        }
        help_texts = {
            'name' : 'Enter the Album Name',
            'musician' : 'Enter the Musician Name',
            'release_date' : 'Enter the Released On',
            'rating' : 'Enter the Rating',
        }
        error_messages = {
            'name': {
                'required' : 'Album Name is required',
            },
            'musician': {
                'required' : 'Musician Name is required',
            },
            'release_date': {
                'required' : 'Released On is required',
            },
            'rating': {
                'required' : 'Rating is required',
            }
        }