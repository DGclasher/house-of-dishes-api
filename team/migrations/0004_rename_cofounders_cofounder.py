# Generated by Django 4.2.4 on 2023-08-30 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_delete_employeetask_cofounders_profile_picture_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoFounders',
            new_name='CoFounder',
        ),
    ]
