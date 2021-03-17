from rest_framework import serializers
from .models import Blog
class BlogSerialzer(serializers.ModelSerializer):
    """Serializer for Agreement Template specific fields"""

    class Meta:
        model = Blog
        fields = ('content',)