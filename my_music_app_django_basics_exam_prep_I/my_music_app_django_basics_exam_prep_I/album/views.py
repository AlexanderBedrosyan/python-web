from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .forms import AlbumForm
from .models import Album
from ..profle.models import Profile


# Create your views here.

class AddView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album-add.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.all().last()
        album_name = request.POST.get('album_name')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        image = request.POST.get('image')
        price = request.POST.get('price')
        album = Album(
            album_name=album_name,
            artist=artist,
            genre=genre,
            description=description,
            image=image,
            price=price,
            owner=profile
        )

        if album:
            album.save()
            return redirect(self.success_url)
        return render(request, 'album-add.html', context={'form': AlbumForm})

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class DetailsView(DetailView):
    model = Album
    template_name = 'album-details.html'
    context_object_name = 'album'


class EditView(UpdateView):
    fields = '__all__'
    model = Album
    template_name = 'album-details.html'


class DeleteAlbumView(DeleteView):
    fields = '__all__'
    model = Album
    template_name = 'album-delete.html'