from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('guestbook/', views.guestbook, name = "guestbook"),
    path('guestbook/<int:blog_id>/', views.blogDetailView, name="blogDetail"),
    path('blog/new', views.blogNewView, name="blogNew"),
    path('blog/create', views.blogCreateView, name="blogCreateFn"),
    path('update/<int:blog_id>/', views.update, name = "update"),
    path('delete/<int:blog_id>/', views.delete, name = "delete"),
]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)