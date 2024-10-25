from django import forms
from .models import ToDoList, Book, Person
from django.core.exceptions import ValidationError

class NameForm(forms.Form): # label option
    name = forms.CharField(
        label='Your Name',
        max_length=50
    )

class Url(forms.Form): # Initial argument
    url_path = forms.URLField(
        label='Url Field',
        initial="http://"
    )

class HelpText(forms.Form):
    first_name = forms.CharField(
        help_text="Add your first name",
        max_length=30
    )

class Comment(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea,
        max_length=200
    )

class SelectOptionForm(forms.Form):
    CHOICES = (
        ('1', 'Option One'),
        ('2', 'Option Two')
    )
    choice_field = forms.ChoiceField( # Може да се направи и с CharField
        choices=CHOICES
    )


class RadioButtonForm(forms.Form):
    CHOICES = (
        ('1', 'Option One'),
        ('2', 'Option Two')
    )
    radio_field = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect()
    )

class CheckBoxForm(forms.Form):
    checkbox_field = forms.BooleanField(required=False)


class InheritModelForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        labels = {
            'title': 'Book Title',
            'author': 'Author Name'
        }

        error_messages = {
            'title': {
                'required': 'You must enter a title.',
                'max_length': 'Your length have to be maximum 20 characters.'
            }
        }


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            # self.fields[field_name].widget.attrs['readonly'] = 'readonly'
            self.fields[field_name].required = False
            print(field_name)

    def clean(self):
        cleaned_data = super(PersonForm, self).clean()
        print(cleaned_data['first_name'])
        print(cleaned_data['last_name'])

        if cleaned_data['first_name'] == cleaned_data['last_name']:
            raise ValidationError('Incorrect names')

        return cleaned_data
