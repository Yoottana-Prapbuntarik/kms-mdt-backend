
from rest_framework import status
from rest_framework import generics, permissions
from knox.models import AuthToken
from .models import Blog
from knox.auth import TokenAuthentication

from rest_framework.response import Response
from .serializer import BlogSerialzer, BlogContentViewSerializer
class BlogAPI(generics.CreateAPIView):
    """Create Agreement Content View """
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ permissions.IsAuthenticated,]
    serializer_class = BlogSerialzer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            content = serializer.validated_data.get('content')
            serializer.save(content=content, own_user=self.request.user)
            return Response({'key_message': 'Created blog successfully' , 'status': status.HTTP_200_OK})

        return Response({'key_message': 'CannotCreate'}, status=status.HTTP_400_BAD_REQUEST)
    

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

class BlogContentViewAllAPI(generics.ListAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogContentViewSerializer
    def get_queryset(self):
        """Return objects fot the current authenticated user only"""
        data = self.queryset.all()
        return data

    def list(self, request):
        queryset_list = self.get_queryset().order_by('-pub_date')
        serializer_list = BlogContentViewSerializer(queryset_list, many=True)
        data = {'blog': serializer_list.data}
        return Response(data)