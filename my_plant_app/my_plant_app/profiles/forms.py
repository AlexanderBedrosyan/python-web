from django import forms
from my_plant_app.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileBaseForm):

    class Meta(ProfileBaseForm.Meta):
        exclude = ['profile_picture']


class EditProfileForm(ProfileBaseForm):
    pass