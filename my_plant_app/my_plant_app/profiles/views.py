from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from my_plant_app.plants.models import Plant
from my_plant_app.profiles.forms import CreateProfileForm, EditProfileForm
from my_plant_app.profiles.models import Profile
from my_plant_app.utils import get_user_obj


# Create your views here.

class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')
    form_class = CreateProfileForm


class DetailsProfile(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plants'] = len(Plant.objects.all())
        return context


class EditProfileView(UpdateView):
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('details-profile')
    form_class = EditProfileForm

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_user_obj()

    def form_valid(self, form):
        Plant.objects.all().delete()
        return super().form_valid(form)




def delete_profile(request):
    return render(request, 'profile/delete-profile.html')