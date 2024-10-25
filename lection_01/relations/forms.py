from django import forms
from relations.models import SinglePerson, Rating, Comment


class PersonForm(forms.ModelForm):
    class Meta:
        model = SinglePerson
        fields = '__all__'

        widgets = {
            'description': forms.Textarea(attrs={'placeholder':'Text something about yourself'})
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)])
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['username', 'comment']

        labels = {
            'username': 'Text your username',
            'comment': 'Your comment'
        }