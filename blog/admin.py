from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ['own_user', 'content']
    list_filter = ['own_user', 'content']

    ordering = ('id',)
    
admin.site.register(Blog, BlogAdmin)
