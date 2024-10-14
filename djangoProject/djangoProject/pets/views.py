from django.shortcuts import render, redirect

from .forms import PetEditForm
from .models import Pet
from ..common.forms import CommentForm


# Create your views here.

def add_pets(request):
    return render(request, template_name='pets/pet-add-page.html')

def pets_details(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }

    return render(request, 'pets/pet-details-page.html', context=context)


def edit_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {
        "form": form,
        "pet": pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)

def delete_page(request):
    return render(request, template_name='pets/pet-delete-page.html')