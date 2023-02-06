from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-pk")
    return render(
        request,
        "app/index.html",
        {
            "posts": posts,
        },
    )


def single_post_page(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "app/single_page.html",
        {
            "post": post,
        },
    )
