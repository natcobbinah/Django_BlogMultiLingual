from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm

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
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            return redirect("blog:post_list")
    form = PostForm(instance=post)

    return render(
        request, "blog/post/create_edit_post.html", {"form": form, "instance": post}
    )
