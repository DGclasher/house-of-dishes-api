from PIL import Image
from io import BytesIO
from django.db import models
from users.models import ChefUser

class DishInstruction(models.Model):
    instruction_text = models.TextField()
    time_required = models.IntegerField()

    def __str__(self):
        return self.instruction_text

class Dish(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField(default=False)
    number_of_people = models.IntegerField(default=1, blank=True)
    # instructions = models.ManyToManyField(DishInstruction, related_name='dish')
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
    