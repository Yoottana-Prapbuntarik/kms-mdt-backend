from django.contrib import admin
from .models import DocumentType, DocumentTemplate, DocumentReview
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['document_name',]

admin.site.register(DocumentType, DocumentAdmin)


class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ['document_type', 'document_file', 'document_preview']
    readonly_fields = ('document_preview', )
    list_filter =['department']
    change_form_template="admin/document/upload-document.html"

admin.site.register(DocumentTemplate, DocumentTemplateAdmin)

class DocumentReviewAdmin(admin.ModelAdmin):
    list_display = ['document_type', 'user', 'student_name', 'student_code', 'document_status', 'document_review']
    readonly_fields = ('document_review', )
    list_filter =['department']
    change_form_template="admin/document/upload-document.html"

admin.site.register(DocumentReview, DocumentReviewAdmin)


