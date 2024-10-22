from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from fruitipedia.fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipedia.fruits.models import Fruit
from fruitipedia.utils import get_user_obj


# Create your views here.

class FruitEditView(UpdateView):
    model = Fruit
    form_class = FruitEditForm
    pk_url_kwarg = 'id'
    template_name = 'fruits/edit-fruit.html'
    success_url = reverse_lazy('dashboard')


class FruitDeleteView(DeleteView):
    model = Fruit
    form_class = FruitDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class FruitDetailView(DetailView):
    model = Fruit
    pk_url_kwarg = 'id'
    template_name = 'fruits/details-fruit.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        fruit = Fruit.objects.get(id=self.kwargs[self.pk_url_kwarg])
        contex['fruit'] = fruit
        return contex


class FruitCreateView(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)



def delete_fruit(request, id):
    return render(request, 'fruits/delete-fruit.html')