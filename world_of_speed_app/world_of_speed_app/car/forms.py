from django import forms
from world_of_speed_app.car.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    image = forms.URLField(
        label='Image URL:',
        widget=forms.URLInput(
            attrs={
                'placeholder': 'https://...',
            }
        )
    )
    class Meta(CarBaseForm.Meta):
        exclude = ['owner']


class CarDeleteForm(CarCreateForm):
    class Meta(CarBaseForm.Meta):
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.disabled = True
            field.widget.attrs.update({
            'placeholder': 'https://...'
        })

