from django.shortcuts import render
from django.views.generic import DetailView, DeleteView

from .models import Profile


# Create your views here.
class ProfileDetails(DetailView):
    template_name = 'profile-details.html'


class ProfileDelete(DeleteView):
    fields = '__all__'
    model = Profile
    template_name = 'profile-delete.html'