# Generated by Django 5.0.5 on 2024-05-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
