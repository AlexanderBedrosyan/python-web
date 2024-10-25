from django import forms

from tasty_recipes_app.mixins import PlaceholderMixin, ReadOnlyMixin
from tasty_recipes_app.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCreateForm(PlaceholderMixin, RecipeBaseForm):
    class Meta(RecipeBaseForm.Meta):
        exclude = ['author']


class DeleteRecipeForm(PlaceholderMixin, ReadOnlyMixin, RecipeBaseForm):
    class Meta(RecipeBaseForm.Meta):
        exclude = ['author']