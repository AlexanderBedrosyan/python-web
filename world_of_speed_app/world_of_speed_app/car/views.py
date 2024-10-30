from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView

from world_of_speed_app.car.forms import CarCreateForm, CarDeleteForm
from world_of_speed_app.car.models import Car
from world_of_speed_app.utils import get_user_obj


# Create your views here.
class CatalogueView(TemplateView):
    model = Car
    template_name = 'car/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_cars'] = Car.objects.all()
        return context


class CreateCarView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    pk_url_kwarg = 'id'


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car/car-edit.html'
    pk_url_kwarg = 'id'
    form_class = CarCreateForm
    success_url = reverse_lazy('catalogue')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car-delete.html'
    pk_url_kwarg = 'id'
    form_class = CarDeleteForm
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

