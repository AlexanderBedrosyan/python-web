from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView, DeleteView
from tasty_recipes_app.recipes.forms import RecipeCreateForm, DeleteRecipeForm
from tasty_recipes_app.recipes.models import Recipe
from tasty_recipes_app.utils import get_user_obj


class CatalogueView(TemplateView):
    model = Recipe
    template_name = 'recipe/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_recipies = Recipe.objects.all()
        context['recipies'] = all_recipies
        return context


class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class RecipeDetails(DetailView):
    model = Recipe
    pk_url_kwarg = 'id'
    template_name = 'recipe/details-recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = self.kwargs.get(self.pk_url_kwarg)
        current_recipe = Recipe.objects.get(pk=recipe_id)
        context['recipe'] = current_recipe
        context['ingredients'] = current_recipe.ingredients.split(',')
        return context


class EditRecipeView(UpdateView):
    model = Recipe
    pk_url_kwarg = 'id'
    template_name = 'recipe/edit-recipe.html'
    form_class = RecipeCreateForm
    success_url = reverse_lazy('catalogue')


class DeleteRecipeView(DeleteView):
    model = Recipe
    pk_url_kwarg = 'id'
    template_name = 'recipe/delete-recipe.html'
    form_class = DeleteRecipeForm
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)