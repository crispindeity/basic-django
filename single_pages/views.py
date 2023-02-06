from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def landing(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "single_pages/landing.html",
    )


def about_me(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "single_pages/about_me.html",
    )
