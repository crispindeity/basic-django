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
