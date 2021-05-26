from rest_framework import serializers
from .models import Blog, BlogCategory, Comment, ArticleLikeAndUnlike

class getUser(serializers.Field):
    def to_representation(self, value):
        ret = {
            "id": value.own_user.id,
            "first_name": value.own_user.first_name,
            "last_name": value.own_user.last_name,
            "email": value.own_user.email,
            "image": value.own_user.image
        }
        return ret

class BlogSerialzer(serializers.ModelSerializer):
    """Serializer for Agreement Template specific fields"""

    class Meta:
        model = Blog
        fields = ('content', 'own_user', 'category', 'title',  'sub_title', 'cover')

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


class getUserComment(serializers.Field):
    def to_representation(self, value):
        ret = {
            "id": value.user_comment.id,
            "first_name": value.user_comment.first_name,
            "last_name": value.user_comment.last_name,
            "email": value.user_comment.email,
            "image": value.user_comment.image
        }
        return ret
class GetBlogCommentSerializers(serializers.ModelSerializer):
    user_comment = getUserComment(source='*')
    class Meta:
        model = Comment
        fields = ('article', 'user_comment', 'content', 'published')
class BlogCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('article', 'user_comment', 'content',)


class ArticleLikeAndUnlikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleLikeAndUnlike
        fields = ('__all__')