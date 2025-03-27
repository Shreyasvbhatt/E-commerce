from rest_framework import viewsets
from .models import User, Product_table, Order_table, Payment_table
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, PaymentSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Shreyas and Adharsh 1st project"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
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

