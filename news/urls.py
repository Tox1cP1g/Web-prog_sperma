from django.urls import path, re_path
from django.conf.urls import include
from django.views.generic import ListView, DetailView
from news.models import Articles
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    re_path('^(?P<pk>\d+)/$', DetailView.as_view(model=Articles, template_name="news/post.html")),
    path('like/<int:article_id>/', views.like_task, name='like_task'),
    path('likes/', views.get_likes_count, name='likes_all'),
]

