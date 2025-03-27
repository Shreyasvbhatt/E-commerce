from rest_framework import serializers
from .models import User, Product_table, Order_table, Payment_table

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = '__all__'  

class ProductSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Product_table
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Order_table
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Payment_table
        fields = '__all__'
