# Generated by Django 4.2.7 on 2023-11-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custuser',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
