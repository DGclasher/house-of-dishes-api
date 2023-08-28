from django.db import models
from users.models import ChefUser

class Dish(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    chef = models.ForeignKey(ChefUser, on_delete=models.CASCADE, related_name='dish_set')
    VEG_NON_VEG_CHOICES = (
        ('Veg', 'Vegetarian'),
        ('NonVeg', 'Non-Vegetarian'),
    )
    veg_non_veg = models.CharField(max_length=7, choices=VEG_NON_VEG_CHOICES, default='Veg')
    popularity_state = models.CharField(max_length=100, blank=True)
    cuisine = models.CharField(max_length=100, blank=True)
    COURSE_CHOICES = (
        ('MainCourse', 'Main Course'),
        ('Starter', 'Starter'),
        ('Dessert', 'Dessert'),
    )
    main_course_starter_dessert = models.CharField(max_length=12, choices=COURSE_CHOICES, default='MainCourse')
    quantity = models.PositiveIntegerField(default=False)
    customizable_ingredients = models.BooleanField(default=False)
    cooking_time = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
