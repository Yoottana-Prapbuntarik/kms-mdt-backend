from django.urls import path, include
from .api import BlogAPI
urlpatterns = [
    path('api/blog', BlogAPI.as_view()),
]
