from django.contrib import admin
from .models import ArticleNews
# Register your models here.

class ArticleNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'cover_preview',]
    readonly_fields=('cover_preview',)
    change_form_template="admin/news/new-upload-image.html"
    
admin.site.register(ArticleNews, ArticleNewsAdmin)