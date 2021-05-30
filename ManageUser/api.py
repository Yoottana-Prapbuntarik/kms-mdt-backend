from rest_framework import generics, permissions
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework import status, views, viewsets, mixins
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, UserProfileSerializer, Test
from rest_framework.response import Response
from rest_framework import status


class Test(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        
        return Response({"test": "test"})

    def post(self, request, *args, **kwargs):
        
        return Response({"post": "post"})

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"data": "Created User Successful.", "token": AuthToken.objects.create(user)[1]}, status=status.HTTP_201_CREATED)

# Login api
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({"token": AuthToken.objects.create(user)[1], "email": self.request.data['email']}, status=status.HTTP_200_OK)

# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  authentication_classes = (TokenAuthentication,)

  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

class GetUserProfileAPI(generics.ListAPIView):
  permission_classes = [
      permissions.IsAuthenticated,
    ]

  authentication_classes = (TokenAuthentication,)
  serializer_class = UserSerializer
  def get_queryset(self):
      queryset = User.objects.filter(first_name=self.kwargs['first_name']).filter(last_name=self.kwargs['last_name']).filter(id=self.kwargs['id'])
      return queryset


class UserProfileAPI(generics.RetrieveUpdateAPIView, mixins.UpdateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.filter(email=self.request.user)
        return queryset

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):

        return self.partial_update(request, *args, **kwargs)
