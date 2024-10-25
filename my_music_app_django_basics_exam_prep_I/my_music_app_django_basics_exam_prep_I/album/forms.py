from django import forms
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator

from .models import Album
from ..profle import models
from ..profle.models import Profile


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'genre', 'description', 'image', 'price']
        exclude = ['owner']

    labels = {
        'album_name': 'Album Name',
        'artist': 'Artist',
        'genre': 'Genre',
        'description': 'Description',
        'image': 'Album Cover Image',
        'price': 'Price (in $)',
    }

    help_texts = {
        'album_name': 'The name of the album (must be unique).',
        'artist': 'Name of the artist.',
        'genre': 'Select the genre of the album.',
        'price': 'Price must be a positive value.',
    }

    error_messages = {
        'album_name': {
            'unique': 'This album name is already in use. Please choose another one.',
            'required': 'Album name is required.',
            'max_length': 'Only 30 characters'
        },
        'artist': {
            'required': 'Artist name is required.',
        },
        'genre': {
            'required': 'Please select a genre.',
        },
        'image': {
            'required': 'Please upload an album cover image.',
        },
        'price': {
            'required': 'Please specify the price.',
            'invalid': 'Invalid price. Please enter a valid number.',
            'min_value': 'Price must be at least 0.0.',
        },
    }

    GENRE_CHOICES = [
        ('', '-------'),
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other")]

    def clean_album_name(self):
        album_name = self.cleaned_data.get('album_name')
        if Album.objects.filter(album_name=album_name).exists():
            raise forms.ValidationError('This album name is already in use. Please choose another one.')
        if len(album_name) > 30:
            raise forms.ValidationError(self.fields['album_name'].error_messages['max_length'])
        return album_name

    album_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Album Name'
        })
    )
    artist = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Artist'
        })
    )
    genre = forms.ChoiceField(
        required=True,
        choices=GENRE_CHOICES
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Description'
        })
    )
    image = forms.URLField(
        required=True,
        widget=forms.URLInput(attrs={
            'placeholder': 'Image URL'
        })
    )
    price = forms.FloatField(
        required=True,
        validators=[MinValueValidator(0.0)],
        widget=forms.NumberInput(attrs={
            'placeholder': 'Price'
        })
    )
    owner = forms.ModelChoiceField(
        queryset=Profile.objects.all(),
        widget=forms.HiddenInput()
    )
