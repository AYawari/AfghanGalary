# Generated by Django 4.0.2 on 2022-09-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Men", "Men"),
                    ("Women", "Womem"),
                    ("Chose", "Shose"),
                    ("Watch", "Watch"),
                    ("Bag", "Bag"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]
