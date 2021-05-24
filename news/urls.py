from django.urls import path
from . import views
from .api import NewsViewAllAPI
urlpatterns = [
     # path('api/news/<int:pk>', GetBlogCommentViewAPI.as_view()),
     path('api/news', NewsViewAllAPI.as_view()),

     path('upload-images-new', views.uploadImageNews, name="upload-images-new"),
]