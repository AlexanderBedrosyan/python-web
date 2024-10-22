from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia.profiles.forms import ProfileBaseForm, ProfileEditForm
from fruitipedia.profiles.models import Profile
from fruitipedia.utils import get_user_obj


# Create your views here.

class ProfileDetailView(DetailView):
    template_name = 'profile/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileBaseForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_user_obj()

class ProfileDeleteView(DeleteView):
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index-page')

    def get_object(self, queryset=None):
        return get_user_obj()

