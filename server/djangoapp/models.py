from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return "Name: " + self.name + " Description: " + self.description


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        default='SUV'
    )
    year = models.IntegerField(default=2024,
                                validators=[
                                    MaxValueValidator(2024),
                                    MinValueValidator(2015)
                                ])

    def __str__(self):
        return "Name: " + self.name + \
               " Type: " + self.type + \
               " Year: " + str(self.year)
