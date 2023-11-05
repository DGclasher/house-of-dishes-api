from PIL import Image
from io import BytesIO
from django.db import models
from users.models import ChefUser

class Instructions(models.Model):
    step = models.CharField(blank=False, max_length=200)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE, related_name='instructions')
    instruction_video_url = models.CharField(max_length=500, blank=True)

    def __str__(self) -> str:
        return f"{self.step}"

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(blank=False)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self) -> str:
        return f"Name: {self.name} Quantity: {self.quantity}"

class Dish(models.Model):
    name = models.CharField(max_length=100)
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
    course_type = models.CharField(max_length=12, choices=COURSE_CHOICES, default='MainCourse')
    cooking_time = models.CharField(blank=True, default=None, max_length=10)
    dish_picture = models.ImageField(upload_to="dish_images/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.dish_picture:
            image = Image.open(self.dish_picture)
            output_io = BytesIO()
            image = image.resize((600, 400))
            image.save(output_io, format='JPEG', quality=70)
            self.dish_picture.file = output_io
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
