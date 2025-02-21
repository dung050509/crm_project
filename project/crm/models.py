from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Employee(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

class TaskBoard(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('INPROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices= STATUS_CHOICES ,default='TODO')
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)