from django.db import models
from django.utils.safestring import mark_safe





class ArticleNews(models.Model):
    cover_url = models.CharField(max_length=255, null=False, blank=False, default="")
    title = models.CharField(max_length=255, null=False, blank=False, default="")
    sub_title = models.CharField(max_length=255, null=False, blank=False, default="")
    images_article_url = models.CharField(max_length=255, null=True, blank=True, default="")
    detail = models.TextField(null=False, blank=False, default="")
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "บทความข่าวสาร"
    def cover_preview(self):
        return mark_safe('<img src="%s" width="350px"/>' % self.cover_url)

