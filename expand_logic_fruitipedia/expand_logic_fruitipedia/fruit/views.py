from django.shortcuts import render

# Create your views here.


def create_fruit(request):
    return render(request, 'fruit/create-fruit.html')


def fruit_details(request, id):
    return render(request, 'fruit/details-fruit.html')


def fruit_edit(request, id):
    return render(request, 'fruit/edit-fruit.html')


def fruit_delete(request, id):
    return render(request, 'fruit/delete-fruit.html')