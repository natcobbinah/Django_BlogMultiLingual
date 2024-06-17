from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publication_date", "created", "updated"]
    list_filter = ["created", "author", "publication_date"]
    search_fields = ["title", "content"]
    date_hierarchy = "publication_date"
    ordering = ["publication_date"]
    raw_id_fields = ["author"]
