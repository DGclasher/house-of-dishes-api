# Generated by Django 4.2.4 on 2023-11-02 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dish",
            name="customizable_ingredients",
        ),
    ]
