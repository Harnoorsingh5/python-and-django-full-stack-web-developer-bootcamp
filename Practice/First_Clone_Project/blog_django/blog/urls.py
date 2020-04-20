"""blog_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog.views import AboutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, DraftListView, add_comment_to_post, comment_approve, comment_remove, post_publish

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove', comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),
]
