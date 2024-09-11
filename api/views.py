from rest_framework import viewsets
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """User ViewSet
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Post ViewSet
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Comment ViewSet
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionViewSet(viewsets.ModelViewSet):
    """Reaction ViewSet
    """
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """Follow ViewSet
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
