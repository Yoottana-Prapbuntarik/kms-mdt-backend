from rest_framework import serializers

from .models import ServiesUpload

class ServicesUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiesUpload
        fields = ('file', 'remark',)
