from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import User

class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(
        style={'input_type': 'password'},
        label="New Password",
        write_only=True,
        min_length=8
    )
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'},
        min_length=8
    )

    
class Test(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name',)
        
# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','first_name',  'last_name', 'date_joined', 'mobile', 'is_staff', 'image')


# Register
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'email', 'mobile', 'first_name', 'last_name', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(
    email = validated_data['email'],
    mobile = validated_data['mobile'],
    first_name=validated_data['first_name'],
    last_name=validated_data['last_name'],
    password=validated_data['password']
)
    return user 

# Login Serializer
class LoginSerializer(serializers.Serializer):
          
  email = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")


class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields =  ('id', 'mobile', 'first_name', 'last_name', 'image')
    extra_kwargs = {
    'email': {'required': False},
    'mobile': {'required': False},
    'first_name': {'required': False},
    'last_name':{'required': False}, 
    'password':{'required': False}, 
    }


    
