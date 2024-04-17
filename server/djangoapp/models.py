# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ("Sedan", "Sedan"),
        ("Suv", "Suv"),
        ("Wagon", "Wagon"),
    ]
    type = models.CharField(choices=CAR_TYPES, default="Sedan", max_length=100)
    year = models.IntegerField(
        default=2015, validators=[
            MinValueValidator(2015), MaxValueValidator(2023)]
    )
    ENGINE_TYPE = [
        ("Gasoline", "Gasoline"),
        ("Diesel", "Diesel"),
        ("Hybrid", "Hybrid"),
        ("Electric", "Electric"),
    ]
    engine_type = models.CharField(
        choices=ENGINE_TYPE, default="Gasoline", max_length=50
    )
    TRANS_TYPE = [
        ("Automatic", "Automatic"),
        ("Manual", "Manual"),
    ]
    transmission_type = models.CharField(
        choices=TRANS_TYPE, default="Automatic", max_length=50
    )
    horsepower = models.PositiveIntegerField(default=220)

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"
