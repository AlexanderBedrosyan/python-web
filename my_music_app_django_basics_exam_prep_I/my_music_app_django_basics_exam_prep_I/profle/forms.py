from django import forms
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator

from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'

    username = forms.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex=r'^[A-Za-z0-9_]+$',
                message="Ensure this value contains only letters, numbers, and underscore.",
                code='invalid_username'
            )
        ],
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'id': 'username',
            'type': 'text'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'id': 'email',
            'name': 'email',
            'type': 'text'
        })
    )
    age = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(0)],
        widget=forms.TextInput(attrs={
            'id':'age',
            'name': 'age',
            'type': 'number',
            'min': '0',
            'placeholder': 'Age'
        })
    )