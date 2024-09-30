from django.shortcuts import render

# Create your views here.

def add_pets(request):
    return render(request, template_name='pets/pet-add-page.html')

def pets_details(request):
    return render(request, template_name='pets/pet-details-page.html')

def edit_page(request):
    return render(request, template_name='pets/pet-edit-page.html')

def delete_page(request):
    return render(request, template_name='pets/pet-delete-page.html')