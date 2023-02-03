# Generated by Django 4.0.2 on 2022-09-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_product_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Men", "Men"),
                    ("Women", "Womem"),
                    ("Shose", "Shose"),
                    ("Watch", "Watch"),
                    ("Bag", "Bag"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]