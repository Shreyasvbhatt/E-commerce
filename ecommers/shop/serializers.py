from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product_table, Order_table, Payment_table

User = get_user_model()  # FIXED

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        raise serializers.ValidationError("Invalid credentials")

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Product_table
        fields = '__all__'

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Order_table
        fields = '__all__'

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Payment_table
        fields = '__all__'
