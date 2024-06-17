from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Post(models.Model):
    """
    Blog posts model
    """

    title = models.CharField(_("title"), max_length=250)
    content = models.TextField(_("content"))
    publication_date = models.DateTimeField(default=timezone.now)

    # model field arguments:
    #       auto_now_add => the date will be saved automatically when creating an object
    #       auto_now     => the date will be updated automatically when saving an object
    # author field creates a relationship between users and posts, that will help indicate
    # which user wrote which posts
    #
    # related_name helps to specify the name of the reverse relationships from User to Post.
    # using (user.blog_posts) notation to access related objects
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Meta class defines metada for the model
    #
    # Ordering attribute sorts result by publication_date in descending order, with hypen
    # before field name
    #
    # Index on (publication_date and title) will help improve performance for queries
    # filtering or ordering results by these fields
    class Meta:
        ordering = ["-publication_date"]
        indexes = [
            models.Index(fields=["-publication_date", "title"]),
        ]

    # returns a string with human readable representation of the object
    def __str__(self):
        return str(self.title)

    # get_absolute_url() returns the canonical URL for the object
    # reverse() function builds the URL dynamically using the URL name defined
    # in the URL patterns
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id])
