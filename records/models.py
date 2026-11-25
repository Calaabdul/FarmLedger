from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Produce(models.Model):

    UNIT_CHOICES = [  # noqa: RUF012
        ('kg', 'Kilograms'),
        ('ton', 'Tons'),
        ('bag', 'Bags'),
        ('crate', 'Crates'),
        ('piece', 'Pieces'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='produce_records'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='produce'
    )

    name = models.CharField(max_length=150)

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    unit = models.CharField(
        max_length=20,
        choices=UNIT_CHOICES,
        default='kg'
    )

    price_per_unit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    description = models.TextField(blank=True)

    date_recorded = models.DateField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
