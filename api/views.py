from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets

from posts.models import Post, Comment
from api.serializers import PostSerializer, CommentSerializer
from api.permissions import IsAuthorOrReadOnlyPermission


class APIPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAuthorOrReadOnlyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class APICommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAuthorOrReadOnlyPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_pk'))
        return post.comments.all()
