from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from tasty_recipes_app.profiles.forms import CreateProfileForm, ProfileEditForm
from tasty_recipes_app.profiles.models import Profile
from tasty_recipes_app.utils import get_user_obj


# Create your views here.

class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        return super().form_valid(form)


class ProfileDetailsView(DetailView):
    template_name = 'profile/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_user_obj()