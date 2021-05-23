from django.urls import path
from . import views
urlpatterns = [
    path('upload-category-image', views.uploadImageDocument, name="upload-category-image"),
    path('upload-pdf', views.uploadPdfDocument, name="upload-pdf"),
]