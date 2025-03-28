from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin
from .models import  Product_table, Order_table, Payment_table

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone_number",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product_table)
admin.site.register(Order_table)
admin.site.register(Payment_table)
