from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout

# Create your views here.
def user_registration(request):
    UserModel = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user = UserModel.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
    return render(request, 'user_testing/user_form.html')


def user_login(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return render(request, 'user_testing/login.html')
        UserModel = get_user_model()
        username = request.POST.get('username')
        user = UserModel.objects.get(username=username)
        login(request, user)
    return render(request, 'user_testing/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'user_testing/login.html')