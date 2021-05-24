from django.urls import path
from . import views
from .api import NewsViewAllAPI, NewsViewAPIById
urlpatterns = [
     path('api/news/<int:pk>', NewsViewAPIById.as_view()),
     path('api/news', NewsViewAllAPI.as_view()),

     path('upload-images-new', views.uploadImageNews, name="upload-images-new"),
]