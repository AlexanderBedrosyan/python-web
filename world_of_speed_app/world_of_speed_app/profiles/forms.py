from django import forms
from world_of_speed_app.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileBaseForm):
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput,
        label='Password'
    )

    class Meta(ProfileBaseForm.Meta):
        exclude = ['first_name', 'profile_picture']


class EditProfileForm(ProfileBaseForm):
    pass