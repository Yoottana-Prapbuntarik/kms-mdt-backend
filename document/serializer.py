from rest_framework import serializers
from .models import DocumentReview, DocumentType, DocumentTemplate

class CreateDocumentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentReview
        fields = ('__all__')

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ('__all__')


class getCategory(serializers.Field):
    def to_representation(self, value):
        ret = {
            "id": value.document_type.id,
            "document_name": value.document_type.document_name
        }
        return ret

class DocumentTemplateSerializer(serializers.ModelSerializer):
    document_type =  getCategory(source="*")
    
    class Meta:
        model = DocumentTemplate
        fields = ('__all__')
