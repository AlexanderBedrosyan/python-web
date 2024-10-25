from django import forms
from .models import Hero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'

        labels = {
            'name': 'Your nickname',
            'level': 'Level'
        }

        error_messages = {
            'level': {
                'required': 'You need to add a level'
            }
        }