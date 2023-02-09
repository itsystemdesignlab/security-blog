from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("me/about", views.AboutList.as_view(), name="about"),
    path("me/policy", views.PolicyList.as_view(), name="policy"),
    path("me/contact", views.contact, name="contact"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]