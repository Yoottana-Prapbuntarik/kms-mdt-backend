from rest_framework import serializers
from .models import QuestionTopic, CommentQuestion

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


class getCategory(serializers.Field):
    def to_representation(self, value):
        ret = {
            "id": value.category.id,
            "name": value.category.name,
        }
        return ret
    
class QuestionTopicSerializer(serializers.ModelSerializer):
    """Serializer for Agreement Template specific fields"""

    class Meta:
        model = QuestionTopic
        fields = ('title', 'sub_title', 'question_detail', 'question_image', 'category', 'own_user', )


class QuestionTopicViewSerializer(serializers.ModelSerializer):
    own_user = getUser(source='*')
    category = getCategory(source='*')
    class Meta:
        model = QuestionTopic
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

class GetCommentQuestionCommentSerializers(serializers.ModelSerializer):
    user_comment = getUserComment(source='*')
    class Meta:
        model = CommentQuestion
        fields = ('__all__')

class CommentQuestionCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentQuestion
        fields = ('__all__')