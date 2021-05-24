from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils.safestring import mark_safe





class ArticleNews(models.Model):
    cover_url = models.CharField(max_length=255, null=False, blank=False, default="")
    title = models.CharField(max_length=255, null=False, blank=False, default="")
    sub_title = models.CharField(max_length=255, null=False, blank=False, default="")
    images_article_url_1 = models.CharField(max_length=255, null=True,blank=True, default="", help_text="image url (optional)")
    images_article_url_2 = models.CharField(max_length=255, null=True,blank=True, default="", help_text="image url (optional)")
    images_article_url_3 = models.CharField(max_length=255, null=True,blank=True, default="", help_text="image url (optional)")
    images_article_url_4 = models.CharField(max_length=255, null=True,blank=True, default="", help_text="image url (optional)")
    images_article_url_5 = models.CharField(max_length=255, null=True,blank=True, default="", help_text="image url (optional)")
    create_at = models.DateField(auto_now=True)
    detail = models.TextField(null=False, blank=False, default="")
    hyper_link = models.CharField(max_length=255, null=True,  blank=True, help_text="add your hyper link to readmore")

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "บทความข่าวสาร"
    def cover_preview(self):
        return mark_safe('<img src="%s" width="350px"/>' % self.cover_url)