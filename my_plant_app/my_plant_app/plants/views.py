from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView

from my_plant_app.plants.forms import CreatePlantForm, DisabledForm
from my_plant_app.plants.models import Plant
from my_plant_app.utils import get_user_obj


# Create your views here.


class CreatePlantView(CreateView):
    template_name = 'plant/create-plant.html'
    success_url = reverse_lazy('catalogue')
    model = Plant
    form_class = CreatePlantForm


class DetailsPlantView(DetailView):
    model = Plant
    template_name = 'plant/plant-details.html'
    pk_url_kwarg = 'id'

    def get_context_object_name(self, obj):
        return 'plant'


class EditPlantView(UpdateView):
    model = Plant
    template_name = 'plant/edit-plant.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')
    form_class = CreatePlantForm

    def get_initial(self):
        return self.object.__dict__


class DeletePlantView(DeleteView):
    model = Plant
    pk_url_kwarg = 'id'
    form_class = DisabledForm
    success_url = reverse_lazy('catalogue')
    template_name = 'plant/delete-plant.html'

    def get_initial(self):
        return self.object.__dict__
