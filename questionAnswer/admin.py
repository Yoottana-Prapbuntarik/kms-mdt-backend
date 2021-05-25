from django.contrib import admin
from .models import  CommentQuestion, QuestionTopic
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    model = QuestionTopic
    def has_add_permission(self, request, obj=None):
        return False
    list_display = ['preview_image', 'title', 'sub_title','own_user', 'category']
    list_filter = ['own_user', 'category']
    readonly_fields=("preview_image",)
    ordering = ('id',)
    
admin.site.register(QuestionTopic, QuestionAdmin)
admin.site.register(CommentQuestion)