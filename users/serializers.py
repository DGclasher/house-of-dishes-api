import re
from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

class ChefAccountSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = ChefUser
        fields = ('id', 'email', 'first_name', 'last_name','password', 'password_repeat', 'bio', 'profile_picture')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError("Passwords do not match.")
        if len(data['password']) < 10:
            raise serializers.ValidationError("Password length should be more than equal to 10")
        if not re.findall('\d', data['password']):
            raise serializers.ValidationError("Password must contain atleast 1 digit, 0-9")
        if not re.findall('[A-Z]', data['password']):
            raise serializers.ValidationError("Password must contain atleast 1 uppercase letter, A-Z")
        if not re.findall('[a-z]', data['password']):
            raise serializers.ValidationError("Password must contain atleast 1 lowercase letter, a-z")
        return data

    def create(self, validated_data):
        validated_data.pop('password_repeat', None)
        profile_picture = validated_data.pop('profile_picture', None)
        chef_account = ChefUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            bio=validated_data.get('bio', ''),
        )
        chef_account.set_password(validated_data['password'])
        chef_account.save()
        chefs_group, created = Group.objects.get_or_create(name='Chefs')
        chef_account.groups.add(chefs_group)
        if profile_picture:
            chef_account.profile_picture = profile_picture
            chef_account.save()
        return chef_account

class ChefLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to login with given credentials.")
        else:
            raise serializers.ValidationError("Must include email and password fields.")
        return data

class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField(min_length=5)
    
    class Meta:
        fields = ['email']
    
    def validate(self, validated_data):
        try:
            email = validated_data.get('email')
            if ChefUser.objects.filter(email=email).exists():
                user = ChefUser.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(user.id)
                token = PasswordResetTokenGenerator().make_token(user)


            return validated_data
        except:
            pass