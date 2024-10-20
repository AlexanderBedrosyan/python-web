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
        form = self.get_form()
        print(request.GET.album_name)

        if form.is_valid():
            album = form.save(commit=False)
            album.owner = profile
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