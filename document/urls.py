from django.urls import path
from . import views
from .api import CreateDocumentReviewApi, GetDocumentAPI, DocumentCategoryApi, DocumentTemplateApi, DocumentUpdate, GetDocumentReviewAPI, DeleteDocument, GetDocumentAPIById, GetDocsAllUser

urlpatterns = [
    path('api/document', CreateDocumentReviewApi.as_view()),
    path('api/document/review/all', GetDocumentReviewAPI.as_view()),
    path('api/category', DocumentCategoryApi.as_view()),
    path('api/template', DocumentTemplateApi.as_view()),
    path('api/template/<department>', GetDocumentAPI.as_view()),
    path('api/template/find/<int:id>', GetDocumentAPIById.as_view()),
    # get docs uer
    path('api/document/user', GetDocsAllUser.as_view()),
    # Update or delete
    path('api/template/update/<int:pk>',DocumentUpdate.as_view()),
    path('api/template/delete/<int:pk>',DeleteDocument.as_view()),

    path('upload-category-image', views.uploadImageDocument, name="upload-category-image"),
    path('upload-pdf', views.uploadPdfDocument, name="upload-pdf"),
]