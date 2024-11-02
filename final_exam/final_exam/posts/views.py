from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from final_exam.posts.forms import CreatePostForm, EditPostForm, DeletePostForm
from final_exam.posts.models import Post
from final_exam.utils import get_user_obj


# Create your views here.


class CreatePostView(CreateView):
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')
    model = Post
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class DetailsPostView(DetailView):
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'id'
    model = Post


class EditPostView(UpdateView):
    template_name = 'posts/edit-post.html'
    pk_url_kwarg = 'id'
    model = Post
    form_class = EditPostForm
    success_url = reverse_lazy('dashboard')


class DeletePostView(DeleteView):
    pk_url_kwarg = 'id'
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')
    form_class = DeletePostForm
    model = Post

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


def post_delete(request, id):
    return render(request, 'posts/delete-post.html')