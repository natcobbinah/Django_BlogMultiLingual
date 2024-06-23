from django import forms
from .models import Post

SEARCH_BY_CHOICES = (
    ("title", "Title"),
    ("content", "Content")
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "post_image"]


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_by = forms.ChoiceField(
        required=False,
        choices=SEARCH_BY_CHOICES
    )
