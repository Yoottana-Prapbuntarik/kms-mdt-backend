from django.db import models
from django.conf import settings
from ManageUser.models import User
# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, default="")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "ประเภทบทความ"


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, default="")
    sub_title = models.CharField(max_length=255, blank=False, null=False, default="")
    cover = models.CharField(max_length=255, blank=False, null=False, default="")
    content = models.TextField(null=False, blank=False, default="")
    own_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.content
    class Meta:
        verbose_name_plural = "บทความ"


#  user    comment  article
class Comment(models.Model):
    article = models.ForeignKey(
        Blog,
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
        verbose_name_plural = "ความเห็นบทความ"

