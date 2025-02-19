from django import forms
from my_plant_app.plants.models import Plant


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(BasePlantForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plant_type'].label = 'Type:'


class DisabledForm(BasePlantForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plant_type'].label = 'Type:'

        for field_name, field in self.fields.items():
            field.disabled = True

