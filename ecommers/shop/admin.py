from django.contrib import admin

from django.contrib import admin
from .models import User, Product_table, Order_table, Payment_table

admin.site.register(User)
admin.site.register(Product_table)
admin.site.register(Order_table)
admin.site.register(Payment_table)

