
from rest_framework import status
from rest_framework import generics, permissions
from knox.models import AuthToken
from .models import Blog, BlogCategory
from knox.auth import TokenAuthentication

from rest_framework.response import Response
from .serializer import BlogSerialzer, BlogContentViewSerializer, BlogCategorySerializer 
class BlogAPI(generics.CreateAPIView):
    """Create Agreement Content View """
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ permissions.IsAuthenticated,]
    serializer_class = BlogSerialzer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            content = serializer.validated_data.get('content')
            title = serializer.validated_data.get('title')
            sub_title = serializer.validated_data.get('sub_title')
            cover = serializer.validated_data.get('cover')
            category = serializer.validated_data.get('category')

            serializer.save(content=content, own_user=self.request.user, title = title, sub_title=sub_title,category=category, cover=cover)
            return Response({'key_message': 'Created blog successfully' , 'status': status.HTTP_200_OK})

        return Response({'key_message': 'Cannot Create'}, status=status.HTTP_400_BAD_REQUEST)
    

class BlogContentViewAPI(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]

    queryset = Blog.objects.all()
    serializer_class = BlogContentViewSerializer

    def get_queryset(self):
        """Return objects fot the current authenticated user only"""
        data = self.queryset.filter(own_user=self.request.user)
        return data

    def list(self, request):
        queryset_list = self.get_queryset().order_by('-id')
        serializer_list = BlogContentViewSerializer(queryset_list, many=True)
        data = {'blog': serializer_list.data}
        return Response(data)


class BlogDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogContentViewSerializer

class BlogContentViewAllAPI(generics.ListAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogContentViewSerializer
    def get_queryset(self):
        """Return objects fot the current authenticated user only"""
        
        data = self.queryset.all()
        return data

    def list(self, request):
        queryset_list = self.get_queryset().order_by('-pub_date').filter(published=True)
        serializer_list = BlogContentViewSerializer(queryset_list, many=True)
        data = {'blog': serializer_list.data}
        return Response(data)

class BlogCategoryAPI(generics.ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    def get_queryset(self):
        data = self.queryset.all()
        return data
    
    def list(self, request):
        queryset_list = self.get_queryset().order_by('-id')
        serializer_list = BlogCategorySerializer(queryset_list, many=True)
        data = {'category': serializer_list.data}
        return Response(data)

