from django.urls import path
from app import views

urlpatterns = [
    path("", views.PostList.as_view()),
    path("<int:pk>", views.PostDetail.as_view()),
]
