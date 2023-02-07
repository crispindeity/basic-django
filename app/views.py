from django.views.generic import ListView, DetailView
from app.models import Post


# CBV 방식
class PostList(ListView):
    model = Post
    ordering = "-pk"


# CBV 방식
class PostDetail(DetailView):
    model = Post


# FBV 방식
# def index(request: HttpRequest) -> HttpResponse:
#     posts = Post.objects.all().order_by("-pk")
#     return render(
#         request,
#         "app/index.html",
#         {
#             "posts": posts,
#         },
#     )


# FBV 방식
# def single_post_page(request: HttpRequest, pk: int) -> HttpResponse:
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         "app/single_page.html",
#         {
#             "post": post,
#         },
#     )
