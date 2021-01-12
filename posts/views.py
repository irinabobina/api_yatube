from rest_framework import status, permissions, viewsets
from rest_framework.response import Response

from .models import Post, User, Comment
from .serializers import PostSerializer

class PostsViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.method == 'GET':
            post = Post.objects.all()
            serializer = PostSerializer(
                post,
                data=serializer.data,
                partial=True
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Respomse(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, id):
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            serializer = PostSerializer(
                post,
                data=serializer.data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        if request.method == 'GET':
            serializer = PostSerializer(
                post,
                data=serializer.data,
                partial=True
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

    def put(self, request, id):
        post = Post.objects.get(pk=id)
        if request.method == 'PUT':
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, id):
        post = Post.objects.get(pk=id)
        if request.method == 'PATCH':
            serializer = PostSerializer(
                post,
                data=serializer.data,
                partial=True
            )
            if post.author == request.user:
                if serializer.is_valid():
                    serializer.save(author=request.user)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            return Response(
                status=status.HTTP_403_FORBIDDEN
            )
    def delete(self, request, id):
        post = Post.objects.get(pk=id)
        post.delete()
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)



