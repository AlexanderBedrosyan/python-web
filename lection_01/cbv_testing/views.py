from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import classonlymethod
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Hero
from .forms import HeroForm


# Create your views here.

class BaseView:
    @classonlymethod
    def as_view(cls):
        def view(request, *args, **kwargs):
            view_instance = cls()
            return view_instance.dispatch(request, *args, **kwargs)
        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.get(request, *args, **kwargs)
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)


class IndexTemplateView(TemplateView):
    template_name = 'cbv_testing/index.html'
    extra_context = {
        'hardcode_view': f"IndexTemplateView"
    }

    @property
    def give_me_the_class_name(self):
        return self.__class__.__name__

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = self.give_me_the_class_name
        return context


class HeroCreateView(CreateView):
    fields = '__all__'
    model = Hero
    template_name = 'cbv_testing/create_hero.html'

    def get_success_url(self):
        return reverse('new-hero', kwargs={'hero_id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HeroForm()
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class NewHeroView(TemplateView):
    template_name = 'cbv_testing/new_hero.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hero_id = self.kwargs.get('hero_id')
        context['last_created_hero'] = Hero.objects.get(id=hero_id)
        return context


class AllHeroesView(TemplateView):
    template_name = 'cbv_testing/all_heroes.html'
    extra_context = {
        'heroes': Hero.objects.all().order_by('id')
    }


class EditHeroView(UpdateView):
    model = Hero
    template_name = 'cbv_testing/edit_hero.html'
    fields = '__all__'
    success_url = reverse_lazy('heroes')

    def get_object(self, queryset=None):
        hero_id = self.kwargs.get('hero_id')
        return Hero.objects.get(id=hero_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context