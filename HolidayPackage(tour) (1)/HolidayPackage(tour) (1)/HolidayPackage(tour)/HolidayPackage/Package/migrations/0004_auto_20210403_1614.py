# Generated by Django 3.0.8 on 2021-04-03 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Package', '0003_auto_20210403_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package_details',
            old_name='p_package_travelling',
            new_name='p_travel_through',
        ),
    ]