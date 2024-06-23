from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile
from .models import Post
from .forms import PostForm, SearchForm

# Create your views here.


def post_list(request):
    post_list = Post.objects.all()

    # paginator with 10 posts per page
    paginator = Paginator(post_list, 4)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "blog/post/detail.html", {"post": post})


def post_edit(request, pk=None):
    if pk is not None:
        post = get_object_or_404(Post, pk=pk)
    else:
        post = None

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user

            post_image = form.cleaned_data.get("post_image")
            if post_image and not hasattr(post_image, "path"):
                image = Image.open(post_image)
                image.thumbnail((500, 500))
                image_data = BytesIO()
                image.save(fp=image_data, format=post_image.image.format)
                image_file = ImageFile(image_data)
                new_post.post_image.save(post_image.name, image_file)
            new_post.save()

            return redirect("blog:post_list")
    form = PostForm(instance=post)

    return render(
        request, "blog/post/create_edit_post.html", {
            "form": form,
            "instance": post,
            "is_file_upload": True}
    )


def search_post(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    posts = set()

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_by = form.cleaned_data.get("search_by") or "title"
        if search_by == "title":
            posts = Post.objects.filter(title__icontains=search)
        else:
            posts = Post.objects.filter(content__icontains=search)
    else:
        form = SearchForm()

    return render(request,
                  "search/search-results.html", {
                      "form": form,
                      "search_text": search_text,
                      "posts": posts
                  })
