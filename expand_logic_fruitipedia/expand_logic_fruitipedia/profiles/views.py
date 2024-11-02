from django.shortcuts import render

# Create your views here.
def create_profile(request):
    return render(request, 'profile/create-profile.html')


def details_profile(request):
    return render(request, 'profile/details-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')