import string
import random
from django.db import models

class CoFounders(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class EmployeeTask(models.Model):
    task_description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.task_description


class Employee(models.Model):
    employee_id = models.CharField(max_length=12, unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    feedback = models.TextField(blank=True)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    tasks_assigned = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.employee_id:
            characters = string.ascii_uppercase + string.digits
            self.employee_id = ''.join(random.choice(characters) for _ in range(12))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} : {self.employee_id}"
