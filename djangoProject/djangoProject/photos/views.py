from django.shortcuts import render, redirect

from djangoProject.common.forms import CommentForm
from djangoProject.photos.forms import PhotoEditForm
from djangoProject.photos.models import Photo


# Create your views here.

def add(request):
    return render(request, template_name='photos/photo-add-page.html')

def details(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    comment_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)

def edit(request,  pk: int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {
        "form": form,
        "photo": photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)

