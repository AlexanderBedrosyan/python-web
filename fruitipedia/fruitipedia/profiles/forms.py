from django import forms
from fruitipedia.mixins import PlaceholderMixin, LabelMixin
from fruitipedia.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(PlaceholderMixin, ProfileBaseForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',  # Placeholder
            }
        ),
        help_text='*Password length requirements: 8 to 20 characters',
        label='',
    )


class ProfileEditForm(LabelMixin, ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['image', 'password']