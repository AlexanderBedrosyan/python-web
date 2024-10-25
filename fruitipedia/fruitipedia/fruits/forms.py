from django import forms
from fruitipedia.fruits.models import Fruit
from fruitipedia.mixins import PlaceholderMixin, DisabledMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        exclude = ['owner']


class FruitCreateForm(PlaceholderMixin, FruitBaseForm):
    pass


class FruitEditForm(PlaceholderMixin, FruitBaseForm):
    pass


class FruitDeleteForm(DisabledMixin, FruitBaseForm):
    pass