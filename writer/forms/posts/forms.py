from django import forms
from posts.models import Post
from tinymce.widgets import TinyMCE
from category.models import Topic, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "topic",
            "title",
            "is_editors_choice",
            "tags",
            "content",
            "summary",
            "image",
            "bg_image",
        ]
        widgets={
            "content": TinyMCE(attrs={"class": "form-control content"}),
        }
