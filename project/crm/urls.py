from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, ProductViewSet, EmployeeViewSet, TaskBoardViewSet, RegisterView


router = DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'taskboard', TaskBoardViewSet, basename='taskboard')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
]