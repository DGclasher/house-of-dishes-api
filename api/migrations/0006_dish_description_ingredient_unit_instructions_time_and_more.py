# Generated by Django 4.2.4 on 2023-11-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_dish_course_type_alter_dish_veg_non_veg"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="description",
            field=models.CharField(blank=True, default=None, max_length=500),
        ),
        migrations.AddField(
            model_name="ingredient",
            name="unit",
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name="instructions",
            name="time",
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name="dish",
            name="cooking_time",
            field=models.IntegerField(default=None),
        ),
    ]
