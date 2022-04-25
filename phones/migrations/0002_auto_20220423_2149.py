# Generated by Django 3.2.8 on 2022-04-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
