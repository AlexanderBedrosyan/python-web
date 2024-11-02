from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from final_exam.authors.forms import AuthorCreateForm, EditAuthorForm
from final_exam.authors.models import Author
from final_exam.utils import get_user_obj


# Create your views here.


class CreateAuthorView(CreateView):
    model = Author
    success_url = reverse_lazy('dashboard')
    template_name = 'author/create-author.html'
    form_class = AuthorCreateForm


class DetailsAuthorView(DetailView):
    model = Author
    template_name = 'author/details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_post = self.get_object().posts.all().order_by('update_at').last()
        context['latest_post'] = latest_post
        return context


class EditAuthorView(UpdateView):
    template_name = 'author/edit-author.html'
    form_class = EditAuthorForm
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteAuthorView(DeleteView):
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('index-page')

    def get_object(self, queryset=None):
        return get_user_obj()

def delete_author(request):
    return render(request, 'author/delete-author.html')