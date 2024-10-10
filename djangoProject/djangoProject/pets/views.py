from django.shortcuts import render
from .models import Pet

# Create your views here.

def add_pets(request):
    return render(request, template_name='pets/pet-add-page.html')

def pets_details(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)

    context = {
        'pet': pet
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_page(request):
    return render(request, template_name='pets/pet-edit-page.html')

def delete_page(request):
    return render(request, template_name='pets/pet-delete-page.html')