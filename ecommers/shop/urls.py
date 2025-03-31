from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ProductViewSet, OrderViewSet, PaymentViewSet,
    RegisterView, LoginView, LogoutView, register
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # ✅ API Endpoints
    path('api/register/', RegisterView.as_view(), name='registration_view'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # ✅ Serve HTML Registration Page
    path('register/', register, name='register'),
]
