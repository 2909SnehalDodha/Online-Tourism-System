# Generated by Django 3.0.8 on 2021-04-03 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Package', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package_details',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_title', models.CharField(max_length=30)),
                ('p_price', models.IntegerField()),
                ('p_package_days', models.CharField(max_length=50)),
                ('p_package_travelling', models.CharField(max_length=100)),
                ('p_phone', models.IntegerField()),
                ('p_provider_name', models.CharField(max_length=50)),
                ('p_provider_address', models.CharField(max_length=120)),
                ('p_full_package_description', models.TextField(max_length=255)),
                ('p_package_image', models.ImageField(upload_to='Package/images')),
                ('p_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Package.Packages')),
            ],
        ),
    ]
