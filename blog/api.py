
from rest_framework import status
from rest_framework import generics, permissions
from knox.models import AuthToken
from knox.auth import TokenAuthentication

from rest_framework.response import Response
from .serializer import BlogSerialzer
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
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'key_message': 'CannotCreate'}, status=status.HTTP_400_BAD_REQUEST)
    