from django.utils.safestring import mark_safe
from django.db import models
from django.conf import settings
from ManageUser.models import User
# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, default="")
    cate_image = models.CharField(max_length=255, null=False, blank=False, default="")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "ประเภทบทความ"
    def category_image(self):
        return mark_safe('<img src="%s" width="350px"/>' % self.cate_image)
    category_image.allow_tags = True


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, default="")
    sub_title = models.TextField(blank=False, null=False, default="")
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
        on_delete=models.RESTRICT,
        default=1
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "บทความ"
    def blog_cover(self):
        return mark_safe('<img src="%s" width="350px"/>' % self.cover)
    blog_cover.allow_tags = True

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


class ArticleLikeAndUnlike(models.Model):

    user_like = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    blog_like = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
    )