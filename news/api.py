from rest_framework import status
from rest_framework import generics, permissions
from .models import ArticleNews
from .serializers import ArticleNewsSerializer
from rest_framework.response import Response

# class NewsViewAPIById(generics.ListAPIView):

#     serializer_class = GetBlogCommentSerializers
#     def get_queryset(self):
#         queryset = Comment.objects.filter(article__id=self.kwargs['pk'])
#         return queryset


class NewsViewAllAPI(generics.ListAPIView):

    queryset = ArticleNews.objects.all()
    serializer_class = ArticleNewsSerializer
    def get_queryset(self):        
        data = self.queryset.all()
        return data

    def list(self, request):
        queryset_list = self.get_queryset()
        serializer_list = ArticleNewsSerializer(queryset_list, many=True)
        data = {'news': serializer_list.data}
        return Response(data)