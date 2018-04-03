from django.urls import path

from . import views
from .feeds import LatestPostsFeed


app_name = 'blog_app'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('tag/<tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),

    # post details
    path('<int:year>/<int:month>/<int:day>/<post>', views.post_detail, name='post_detail'),

    # share
    path('<int:post_id>/share/', views.post_share, name='post_share'),

    # feed
    path('feed/', LatestPostsFeed(), name='post_feed'),

    # search
    path('search/', views.post_search, name='post_search'),
]
