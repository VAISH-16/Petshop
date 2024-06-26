# Generated by Django 5.0.4 on 2024-04-24 02:43

import autoslug.fields
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=50)),
                (
                    "category_slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="category_name", unique=True
                    ),
                ),
            ],
        ),
        migrations.AlterModelManagers(
            name="product",
            managers=[
                ("productManager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="products.category",
            ),
        ),
    ]
