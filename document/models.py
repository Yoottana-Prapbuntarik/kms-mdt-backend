from django.db.models.base import Model
from django.db.models.expressions import F
import document
from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings

class DocumentType(models.Model):
    document_name = models.CharField(max_length=255, null=False, blank=False, default="")
    
    def __str__(self):
        return self.document_name
    class Meta:
        verbose_name_plural = "ประเภทบทความ"

class DocumentTemplate(models.Model):
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.RESTRICT
    )

    document_file = models.CharField(max_length=255, null=False, blank=False, default="")
    def __str__(self):
        return self.document_file
    class Meta:
        verbose_name_plural = "เทมเพลตเอกสาร"
    def document_preview(self):
        return mark_safe('<object width="800" height="600" type="application/pdf" data="%s"> <p>Insert your error message here, if the PDF cannot be displayed.</p> </object>' % self.document_file)


class DocumentReview(models.Model):
    STATUS = (
        ('approve', 'Approve'),
        ('reject', 'Reject'),
        ('waiting', 'Waiting')
    )

    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.RESTRICT
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    student_name = models.CharField(max_length=25, null=False, blank=False, default="")
    student_code = models.CharField(max_length=25, null=False, blank=False, default="")
    document_status = models.CharField(max_length=24, null=False, blank=False, default="waiting", choices=STATUS)
    comment = models.TextField(null=True, blank=True)
    document_file_review = models.CharField(max_length=255, null=False, blank=False, default="",)
    def __str__(self):
        return self.document_file_review
    class Meta:
        verbose_name_plural = "ตรวจสอบ / รีวิวเอกสาร"
    def document_review(self):
        return mark_safe('<object width="800" height="600" type="application/pdf" data="%s"> <p>Insert your error message here, if the PDF cannot be displayed.</p> </object>' % self.document_file_review)


