# Generated by Django 4.0.2 on 2022-09-06 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_product_product_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
