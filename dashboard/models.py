from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    CATEGORY = (
        ('Stationary', 'Stationary'),
        ('Electronics', 'Electronics'),
        ('Food', 'Food'),
    )
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(choices=CATEGORY, max_length=20, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = "Product"

    def __str__(self) -> str:
        return f"{self.name}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Order"

    def __str__(self) -> str:
        return f"{self.product} ordered by {self.staff.username}"


