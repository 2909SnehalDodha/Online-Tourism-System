# Generated by Django 3.0.8 on 2021-04-03 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Package', '0004_auto_20210403_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_address', models.CharField(max_length=255)),
                ('booking_phone', models.IntegerField()),
                ('boarding', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('travellers', models.IntegerField()),
                ('room_wise', models.CharField(max_length=50)),
                ('booking_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Package.Package_details')),
                ('booking_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
