from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *

# Main router
routers = DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'posts', PostViewSet)
routers.register(r'comments', CommentViewSet)
routers.register(r'reactions', ReactionViewSet)
routers.register(r'follows', FollowViewSet)

# Nested user routers
users_router = NestedDefaultRouter(routers, r'users', lookup='user')
users_router.register(r'posts', PostViewSet, basename='user-posts')
users_router.register(r'comments', CommentViewSet, basename='user-comments')
users_router.register(r'reactions', ReactionViewSet, basename='user-reactions')
users_router.register(r'follows', FollowViewSet, basename='user-follows')

# Nested post routers
posts_router = NestedDefaultRouter(users_router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')
posts_router.register(r'reactions', ReactionViewSet, basename='post-reactions')

# Nested comment routers
comments_router = NestedDefaultRouter(posts_router, r'comments', lookup='comment')
comments_router.register(r'reactions', ReactionViewSet, basename='comment-reactions')


# Include all routers
urlpatterns = [
    path('', include(routers.urls)),
    path('', include(users_router.urls)),
    path('', include(posts_router.urls)),
    path('', include(comments_router.urls)),
]
