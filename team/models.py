import string
import random
from PIL import Image
from io import BytesIO
from django.db import models

class CoFounder(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='cofounders/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.profile_picture:
            image = Image.open(self.profile_picture)
            image_io = BytesIO()
            image.save(image_io, format='JPEG', quality=60)
            self.profile_picture.file = image_io

        super().save(*args, **kwargs)


class Employee(models.Model):
    employee_id = models.CharField(max_length=12, unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    feedback = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='employees/', null=True, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    tasks_assigned = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.employee_id:
            characters = string.ascii_uppercase + string.digits
            self.employee_id = ''.join(random.choice(characters) for _ in range(12))
        if self.profile_picture:
            image = Image.open(self.profile_picture)
            image_io = BytesIO()
            image.save(image_io, format='JPEG', quality=60)
            self.profile_picture.file = image_io
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} : {self.employee_id}"
