# Generated by Django 5.0.1 on 2024-02-16 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_item_image'),
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadata',
            name='reciever',
        ),
        migrations.AddField(
            model_name='metadata',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='item.item'),
            preserve_default=False,
        ),
    ]
