from django.shortcuts import render
from django.views.generic import TemplateView

from my_plant_app.plants.models import Plant


# Create your views here.


def home_page(request):
    return render(request, 'common/home-page.html')


class CatalogueView(TemplateView):
    template_name = 'common/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plants'] = Plant.objects.all()
        return context

