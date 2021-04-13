from django.contrib import admin

from .models import Blog, BlogCategory, Comment


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    def has_add_permission(self, request, obj=None):
        return False
    list_display = ['title', 'sub_title', 'cover','own_user', 'category']
    list_filter = ['own_user', 'category']
    ordering = ('id',)
    
admin.site.register(Blog, BlogAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    model = BlogCategory
    ordering = ('id',)
    
admin.site.register(BlogCategory, BlogCategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    def has_add_permission(self, request, obj=None):
        return True

    list_display = ['published', 'content', 'user_comment']
    ordering = ('id',)
    
admin.site.register(Comment, CommentAdmin)
