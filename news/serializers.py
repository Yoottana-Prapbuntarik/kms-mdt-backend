from rest_framework import serializers

from .models import ArticleNews


class ArticleNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleNews
        fields = ('__all__')