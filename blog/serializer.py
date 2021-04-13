from rest_framework import serializers
from .models import Blog, BlogCategory


class BlogSerialzer(serializers.ModelSerializer):
    """Serializer for Agreement Template specific fields"""

    class Meta:
        model = Blog
        fields = ('content', 'own_user', 'category', 'title', 'sub_title', 'cover')


class getUser(serializers.Field):
    def to_representation(self, value):
        ret = {
            "id": value.own_user.id,
            "first_name": value.own_user.first_name,
            "last_name": value.own_user.last_name,
        }
        return ret

class getCategory(serializers.Field):
    def to_representation(self, value):
        ret = {
            "id": value.category.id,
            "name": value.category.name,
        }
        return ret

class BlogContentViewSerializer(serializers.ModelSerializer):
    own_user = getUser(source='*')
    category = getCategory(source='*')
    class Meta:
        model = Blog
        fields = ('__all__')
class BlogCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogCategory
        fields = ('__all__')