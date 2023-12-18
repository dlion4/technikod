
from tinymce import widgets
from posts.models import Post
from django import forms


class PostAdminForm(forms.ModelForm):
    

    class Meta:
        model = Post
        fields = "__all__"
        widgets={
            "content": widgets.TinyMCE(attrs={"class": "form-control content"}),
        }
