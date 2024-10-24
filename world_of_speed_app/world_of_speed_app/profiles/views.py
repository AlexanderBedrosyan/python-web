from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView

from world_of_speed_app.profiles.forms import CreateProfileForm, EditProfileForm
from world_of_speed_app.profiles.models import Profile
from world_of_speed_app.utils import get_user_obj


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    success_url = reverse_lazy('catalogue')
    template_name = 'profile/profile-create.html'
    form_class = CreateProfileForm


class ProfileEditView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDetailsView(TemplateView):
    model = Profile
    template_name = 'profile/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        total_car_price = sum([float(car.price) for car in profile.owners.all()])
        context['total_car_price'] = total_car_price
        return context


class ProfileDeleteView(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()
