# Generated by Django 4.0.2 on 2022-09-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="size",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Small", "Small"),
                    ("Medium", "Medium"),
                    ("Larg", "Larg"),
                    ("Xlarg", "Xlarg"),
                    ("FreeSize", "FreeSize"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]