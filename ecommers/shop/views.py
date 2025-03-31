from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect  # ✅ Added redirect
from django.contrib import messages  # ✅ Added for displaying messages
from .models import CustomUser, Product_table, Order_table, Payment_table
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, PaymentSerializer, LoginSerializer

User = get_user_model()  # Ensures consistency with authentication

def home(request):
    return JsonResponse({"message": "Welcome to Shreyas and Adharsh 1st project"})

# ✅ Function-based view for handling registration form submission
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # Validation checks
        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use!")
            return redirect("register")

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.phone_number = phone_number  # Assuming phone_number is in CustomUser
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")  # Redirect to login page after success

    return render(request, "shop/registration.html")  # Renders registration form on GET request

# ✅ API-based registration (No changes, still useful for API users)
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
    queryset = CustomUser.objects.all()
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
