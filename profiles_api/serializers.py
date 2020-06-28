from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our API View"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a User Profile Object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_date):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_date['email'],
            name=validated_date['name'],
            password=validated_date['password']
        )
        return user



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serlizes Profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}



