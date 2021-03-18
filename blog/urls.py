from django.urls import path, include
from .api import BlogAPI, BlogContentViewAPI, BlogContentViewAllAPI
urlpatterns = [
    path('api/blog', BlogAPI.as_view()),
    path('api/blog/all', BlogContentViewAllAPI.as_view()),
    path('api/blog/get', BlogContentViewAPI.as_view())
]
