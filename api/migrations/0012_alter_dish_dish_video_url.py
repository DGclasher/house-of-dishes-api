# Generated by Django 4.2.4 on 2023-10-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_alter_dish_dish_video_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="dish_video_url",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
