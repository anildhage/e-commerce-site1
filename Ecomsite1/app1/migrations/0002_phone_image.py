# Generated by Django 4.0 on 2022-06-17 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
