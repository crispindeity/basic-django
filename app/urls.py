from django.urls import path
from app import views

urlpatterns = [path("", views.PostList.as_view()), path("", views.single_post_page)]
