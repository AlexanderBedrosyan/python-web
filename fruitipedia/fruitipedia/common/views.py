from django.shortcuts import render
from django.views.generic import TemplateView

from fruitipedia.fruits.models import Fruit


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    return render(request, 'common/dashboard.html')

class DashboardView(TemplateView):
    model = Fruit
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        all_fruits = Fruit.objects.all()
        contex['fruits'] = all_fruits
        return contex