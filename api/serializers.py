from rest_framework import serializers
from .models import Geo, Address, User, Post, Comment, Reaction, Follow


class GeoSerializer(serializers.ModelSerializer):
    """Geo Serializer
    """
    class Meta:
        """Meta class for GeoSerializer
        """
        model = Geo
        fields = ['id', 'latitude', 'longitude', 'created_at', 'updated_at']


class AddressSerializer(serializers.ModelSerializer):
    """Address Serializer
    """
    geo = GeoSerializer(read_only=True)

    class Meta:
        """Meta class for AddressSerializer
        """
        model = Address
        fields = [
            'id',
            'street',
            'city',
            'zipcode',
            'geo',
            'created_at',
            'updated_at']


class UserSerializer(serializers.ModelSerializer):
    """User Serializer
    """
    address = AddressSerializer(read_only=True)

    class Meta:
        """Meta class for UserSerializer
        """
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'date_of_birth',
            'bio',
            'profile_picture',
            'address',
            'created_at',
            'updated_at',
            'is_active']


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer
    """
    user = UserSerializer(read_only=True)

    class Meta:
        """Meta class for PostSerializer
        """
        model = Post
        fields = [
            'id',
            'user',
            'user_id',
            'title',
            'content',
            'image',
            'created_at',
            'updated_at',
            'is_active']


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer
    """
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        """Meta class for CommentSerializer
        """
        model = Comment
        fields = [
            'id',
            'user',
            'post',
            'content',
            'image',
            'created_at',
            'updated_at',
            'is_active']


class ReactionSerializer(serializers.ModelSerializer):
    """Reaction Serializer
    """
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        """Meta class for ReactionSerializer
        """
        model = Reaction
        fields = [
            'id',
            'user',
            'post',
            'created_at',
            'updated_at']


class FollowSerializer(serializers.ModelSerializer):
    """Follow Serializer
    """
    follower = UserSerializer(read_only=True)
    following = UserSerializer(read_only=True)

    class Meta:
        """Meta class for FollowSerializer
        """
        model = Follow
        fields = [
            'id',
            'follower',
            'following',
            'created_at',
            'updated_at']
