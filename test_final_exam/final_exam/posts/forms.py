from django import forms

from final_exam.mixins import ReadOnlyMixin
from final_exam.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CreatePostForm(PostBaseForm):
    title = forms.CharField(
        label='Title:',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Put an attractive and unique title..."
            }
        )
    )
    image_url = forms.CharField(
        label='Post Image Url:',
        help_text="Share your funniest furry photo URL!",
    )

    content = forms.CharField(
        label='Content:',
        widget=forms.Textarea(
            attrs={
                'placeholder': "Share some interesting facts about your adorable pets..."
            }
        )
    )

    class Meta(PostBaseForm.Meta):
        exclude = ['author']


class EditPostForm(PostBaseForm):
    title = forms.CharField(
        label='Title:',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Put an attractive and unique title..."
            }
        )
    )
    image_url = forms.CharField(
        label='Post Image Url:',
        widget=forms.URLInput(
            attrs={
                'placeholder': "Put an attractive and unique title..."
            }
        )
    )

    content = forms.CharField(
        label='Content:',
        widget=forms.Textarea(
            attrs={
                'placeholder': "Share some interesting facts about your adorable pets..."
            }
        )
    )

    class Meta(PostBaseForm.Meta):
        exclude = ['author']


class DeletePostForm(ReadOnlyMixin, PostBaseForm):
    image_url = forms.CharField(
        label='Post Image Url:',
        )

    class Meta(PostBaseForm.Meta):
        exclude = ['author']