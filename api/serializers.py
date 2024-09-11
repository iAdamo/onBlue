from rest_framework import serializers
from .models import Geo, Address, User, Post, Comment, Reaction, Follow


class GeoSerializer(serializers.ModelSerializer):
    """Geo Serializer
    """
    class Meta:
        """Meta class for GeoSerializer
        """
        model = Geo
        fields = ['id', 'latitude', 'longitude']


class AddressSerializer(serializers.ModelSerializer):
    """Address Serializer
    """
    geo = GeoSerializer(read_only=True)
    geo_id = serializers.PrimaryKeyRelatedField(
        queryset=Geo.objects.all(), source='geo', write_only=True)

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
            'geo_id']


class UserSerializer(serializers.ModelSerializer):
    """User Serializer
    """
    address = AddressSerializer(read_only=True)
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(), source='address', write_only=True)

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
            'address_id']


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer
    """
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True)
    image = serializers.ImageField(required=False)

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
            'image']


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer
    """
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True)
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source='post', write_only=True)

    class Meta:
        """Meta class for CommentSerializer
        """
        model = Comment
        fields = [
            'id',
            'user',
            'user_id',
            'post_id',
            'content',
            'image']


class ReactionSerializer(serializers.ModelSerializer):
    """Reaction Serializer
    """
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True)
    post = PostSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source='post', write_only=True)

    class Meta:
        """Meta class for ReactionSerializer
        """
        model = Reaction
        fields = [
            'id',
            'user',
            'user_id',
            'post',
            'post_id']


class FollowSerializer(serializers.ModelSerializer):
    """Follow Serializer
    """
    follower = UserSerializer(read_only=True)
    follower_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='follower', write_only=True)
    following = UserSerializer(read_only=True)
    following_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='following', write_only=True)

    class Meta:
        """Meta class for FollowSerializer
        """
        model = Follow
        fields = [
            'id',
            'follower',
            'follower_id',
            'following',
            'following_id']
