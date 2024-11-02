from django.shortcuts import render
from django.views.generic import TemplateView

from final_exam.posts.models import Post


# Create your views here.


class IndexPage(TemplateView):
    template_name = 'common/index.html'


class DashboardView(TemplateView):
    template_name = 'common/dashboard.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = []

        for post in Post.objects.all():
            value = ''
            curr_content = post.content.split(' ')

            if len(curr_content) <= 3:
                value = post.content
            else:
                value = ' '.join(curr_content[:3])

            context['posts'].append(
                {
                    'id': post.id,
                    'image_url': post.image_url,
                    'title': post.title,
                    'content': value,
                    'real_content': post.content
                }
            )
        return context

