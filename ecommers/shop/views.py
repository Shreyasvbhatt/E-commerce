from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from .models import CustomUser, Product_table, Order_table, Payment_table
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, PaymentSerializer, LoginSerializer

User = get_user_model()  # Ensures consistency with authentication

def home(request):
    return JsonResponse({"message": "Welcome to Shreyas and Adharsh 1st project"})

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "refresh": serializer.validated_data["refresh"],
            "access": serializer.validated_data["access"]
        }, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()  # Use CustomUser instead of User
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product_table.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order_table.objects.all()
    serializer_class = OrderSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment_table.objects.all()
    serializer_class = PaymentSerializer
