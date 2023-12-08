"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from hello import views

posts_patterns = [
    path('', views.posts),
    path('top', views.top),
    path('last', views.last),
    path('all', views.all),
]


post_patterns = [
    path('comments', views.comments),
    path('likes', views.likes),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("posts/", views.posts),
    path("post/<int:id>/", include(post_patterns)),
    path("user/", views.user),
    path("about/", views.about),
    path("contacts/", views.contacts),
    path("details/", views.details),
    path('access/', views.access_page),
    path("json/", views.json),
    path("set/", views.set),
    path("get/", views.get),
]
