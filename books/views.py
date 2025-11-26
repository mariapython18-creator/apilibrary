
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q  #
from .models import Book
from .serializers import Booksserializer, UserSerializer


class Booksoperations(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]  # ✅ Good practice
    queryset = Book.objects.all()
    serializer_class = Booksserializer


class LogoutAPI(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()
            return Response({'msg': 'Logout Successfully'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Token not found'}, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SearchAPIView(APIView):
    def get(self, request):
        q = request.query_params.get('search')
        if q:
            b = Book.objects.filter(
                Q(title__icontains=q) |
                Q(author__icontains=q) |
                Q(language__icontains=q)
            )
            serializer = Booksserializer(b, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'No search query provided'}, status=status.HTTP_400_BAD_REQUEST)
