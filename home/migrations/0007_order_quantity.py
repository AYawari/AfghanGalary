# Generated by Django 4.0.2 on 2022-09-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
