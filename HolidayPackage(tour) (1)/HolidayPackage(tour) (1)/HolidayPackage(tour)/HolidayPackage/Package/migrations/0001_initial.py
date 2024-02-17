# Generated by Django 3.0.8 on 2021-04-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('package', models.CharField(max_length=100)),
                ('p_image', models.ImageField(upload_to='Package/images')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]