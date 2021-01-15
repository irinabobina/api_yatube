from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


from .models import Post, User, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = permission_classes = [IsAuthenticatedOrReadOnly]
    def list(self, request, post_id=None):
        queryset = Post.objects.filter(post=post_id)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request, post_id=None):
        post = get_object_or_404(Post, pk=post_id)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, post_id=None, pk=None):
        post = get_object_or_404(self.queryset, post=post_id, pk=pk) #!
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def update(self, request, post_id=None, pk=None):
        post = get_object_or_404(self.queryset, post=post_id, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if post.author != request.user:
            return Response(request.data, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self, request, post_id=None, pk=None):
        post = get_object_or_404(self.queryset, post=post_id, pk=pk)
        serializer = PostSerializer(
            post, data=request.data, partial=True)
        if post.author != request.user:
            return Response(request.data, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, post_id=None, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        if post.author != request.user:
            return Response(request.data, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,
                      IsOwnerOrReadOnly]
    def list(self, request, post_id=None):
        queryset = Comment.objects.filter(post=post_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request, post_id=None):
        post = get_object_or_404(Post, pk=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, post_id=None, pk=None):
        comment = get_object_or_404(self.queryset, post=post_id, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def update(self, request, post_id=None, pk=None):
        comment = get_object_or_404(self.queryset, post=post_id, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if comment.author != request.user:
            return Response(request.data, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self, request, post_id=None, pk=None):
        comment = get_object_or_404(self.queryset, post=post_id, pk=pk)
        serializer = CommentSerializer(
            comment, data=request.data, partial=True)
        if comment.author != request.user:
            return Response(request.data, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, post_id=None, pk=None):
        comment = get_object_or_404(self.queryset, pk=pk)
        if comment.author != request.user:
            return Response(request.data, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)