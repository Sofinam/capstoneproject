# Generated by Django 5.1.7 on 2025-03-30 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_inventory_user_inventory_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
