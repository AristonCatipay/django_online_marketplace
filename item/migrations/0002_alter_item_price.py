# Generated by Django 4.2.7 on 2023-11-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
