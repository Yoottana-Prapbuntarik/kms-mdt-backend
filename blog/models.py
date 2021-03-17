from django.db import models
from django.conf import settings
from ManageUser.models import User
# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)


class Blog(models.Model):
    content = models.TextField(null=False, blank=False, default="")
    own_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
