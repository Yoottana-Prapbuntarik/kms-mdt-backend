from django.urls import path
from .api import ServicesUploadAPI

urlpatterns = [
    path('api/upload', ServicesUploadAPI.as_view()),
]