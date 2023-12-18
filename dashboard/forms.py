from django import forms
from tinymce.widgets import TinyMCE
from posts.models import Post
from accounts.models import Profile


class PostRegularForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["topic"].empty_label = None
        # self.fields["tags"].empty_label = None

    class Meta:
        exclude = [
            "writer",
            "views",
            "comments",
            "is_approved",
            "is_editors_choice",
            # "tags",
        ]

        model = Post

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "post title testing"}
            ),
            # "topic": forms.TextInput(
            #     attrs={"class": "form-control", "placeholder": "post title testing"}
            # ),
            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "simple post summary. Max words 300",
                    "rows": "5",
                    "cols": "30",
                }
            ),
            "image": forms.FileInput(attrs={"class": ""}),
            "bg_image": forms.FileInput(
                attrs={
                    "class": "",
                    "placeholder": "",
                }
            ),
            "content": TinyMCE(attrs={"class": "form-control content"}),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        fields = ["first_name", "last_name", "avatar", "bio"]
        model = Profile

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "avatar": forms.FileInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "4",
                    "placeholder": "small description about you...(max wo 200)",
                }
            ),
        }
