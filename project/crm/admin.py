from django.contrib import admin
from .models import Customer, Product, Employee, TaskBoard
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')

class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_to')
    search_fields = ('title', 'status')
    list_filter = ('status', 'assigned_to')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TaskBoard, TaskBoardAdmin)