from django.core.exceptions import PermissionDenied
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            if self.request.user.is_staff or self.get_object() == self.request.user:
                return [permissions.IsAuthenticated()]
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def perform_update(self, serializer):
        if self.request.user.is_staff or self.get_object() == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You haven't got access rights to edit this profile.")
