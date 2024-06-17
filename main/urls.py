from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:id>/", views.post_detail, name="post_detail"),
    path(_("post/new/"), views.post_edit, name="post_create"),
    path(_("post/<int:pk>/"), views.post_edit, name="post_update"),
]
