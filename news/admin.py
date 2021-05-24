from django.contrib import admin
from .models import ArticleNews
# Register your models here.

class ArticleNewsAdmin(admin.ModelAdmin):
    list_display = ['cover_preview', 'title', 'sub_title',]
    readonly_fields=('cover_preview',)
    change_form_template="admin/news/new-upload-image.html"
    
admin.site.register(ArticleNews, ArticleNewsAdmin)
