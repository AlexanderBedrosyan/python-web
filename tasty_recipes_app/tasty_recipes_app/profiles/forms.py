from django import forms

from tasty_recipes_app.mixins import PlaceholderMixin
from tasty_recipes_app.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['bio']


class ProfileEditForm(PlaceholderMixin, ProfileBaseForm):
    pass
