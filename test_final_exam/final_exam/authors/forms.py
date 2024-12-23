from django import forms
from final_exam.authors.models import Author
from final_exam.mixins import PlaceholderMixin


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorCreateForm(PlaceholderMixin, AuthorBaseForm):
    passcode = forms.CharField(
        label="Passcode:",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter 6 digits...'
        }),
        help_text="Your passcode must be a combination of 6 digits",
    )

    class Meta(AuthorBaseForm.Meta):
        exclude = ['info', 'image_url']

    def clean_passcode(self):
        passcode = self.cleaned_data.get('passcode')
        if len(passcode) != 6 and not passcode.isdigit():
            raise forms.ValidationError("Your passcode must be exactly 6 digits!")
        return passcode


class EditAuthorForm(AuthorBaseForm):
    image_url = forms.CharField(
        label="Profile Image URL:",
        required=False
    )

    class Meta(AuthorBaseForm.Meta):
        exclude = ['passcode']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = field.label.title()