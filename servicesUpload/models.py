from django.db import models

# Create your models here.
class ServiesUpload(models.Model):
    file = models.FileField(blank=False, null=False, default="", upload_to='blog/')
    remark = models.CharField(max_length=20, default="")
    timestamp = models.DateTimeField(auto_now_add=True)
