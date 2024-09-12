from django.core.exceptions import PermissionDenied
from rest_framework import generics, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            if self.request.user.is_staff or self.get_object().author == self.request.user:
                return [permissions.IsAuthenticated()]
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            if self.request.user.is_staff or self.get_object().author == self.request.user:
                return [permissions.IsAuthenticated()]
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_update(self, serializer):
        if self.request.user.is_staff or self.get_object().author == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You haven't got access rights to edit this post.")

    def perform_destroy(self, instance):
        if self.request.user.is_staff or instance.author == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You haven't got access rights to delete this post.")


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            if self.request.user.is_staff or self.get_object().author == self.request.user:
                return [permissions.IsAuthenticated()]
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            if self.request.user.is_staff or self.get_object().author == self.request.user:
                return [permissions.IsAuthenticated()]
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_update(self, serializer):
        if self.request.user.is_staff or self.get_object().author == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You haven't got access rights to edit this comment.")

    def perform_destroy(self, instance):
        if self.request.user.is_staff or instance.author == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You haven't got access rights to delete this comment.")
