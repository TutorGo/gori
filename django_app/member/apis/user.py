from django.contrib.auth import get_user_model
from rest_auth.registration.views import RegisterView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from member.serializers import UserSerializer, CustomLoginSerializer

User = get_user_model()

__all__ = (
    'UserProfileView',
    'TutorProfileView',
    'DestroyUserView',
    'CreateDjangoUserView',
    'CreateFacebookUserView',
)


class UserProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class TutorProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class DestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer


class CreateDjangoUserView(RegisterView):
    serializer_class = CustomLoginSerializer
