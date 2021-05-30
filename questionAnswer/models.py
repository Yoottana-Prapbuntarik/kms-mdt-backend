from django.db import models
from django.conf import settings
from blog.models import BlogCategory
from django.utils.safestring import mark_safe

class QuestionTopic(models.Model):
    
    title = models.CharField(max_length=255, null=False, blank=False, default="")
    sub_title = models.CharField(max_length=255, null=False, blank=False, default="")
    question_detail = models.TextField(null=False, blank=False, default="")
    question_image = models.CharField(max_length=255, null=False, blank=False, default="")
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.RESTRICT,
        default=1
    )
    own_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def preview_image(self):
        return mark_safe('<img src="%s" width="350px"/>' % self.question_image)
    preview_image.allow_tags = True
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "คำถามในระบบ"


class CommentQuestion(models.Model):

    question = models.ForeignKey(
        QuestionTopic,
        on_delete=models.CASCADE
    )
    user_comment = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    content = models.TextField(null=False, blank=False, default="")

    published = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
    class Meta:
        verbose_name_plural = "ความคิดเห็นต่อคำถาม"