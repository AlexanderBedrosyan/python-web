from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from my_music_app_django_basics_exam_prep_I.profle.forms import ProfileForm
from my_music_app_django_basics_exam_prep_I.profle.models import Profile


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home-with-profile.html'

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.last()
        if not profile:
            form = ProfileForm()
            return render(request, 'home-no-profile.html', {'form': form})

        return self.render_to_response({'profile': profile})

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request, 'home-no-profile.html', {'form': form})