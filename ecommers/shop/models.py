from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class Product_table(models.Model):
    product_ID = models.AutoField(primary_key=True)  
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.IntegerField()  
    product_description = models.CharField(max_length=200)  

    def __str__(self):
        return self.product_name   


class Order_table(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    order_id = models.AutoField(primary_key=True)  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # FIXED
    product = models.ForeignKey(Product_table, on_delete=models.CASCADE)
    product_count = models.IntegerField()  
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  

    def __str__(self):
        return f"Order {self.order_id} - {self.user.username}"  # FIXED


class Payment_table(models.Model):
    order = models.ForeignKey(Order_table, on_delete=models.CASCADE)  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # FIXED
    product = models.ForeignKey(Product_table, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)  
    transaction_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Transaction {self.transaction_id}"
