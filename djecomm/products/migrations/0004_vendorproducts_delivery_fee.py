# Generated by Django 4.2.8 on 2024-10-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_hsn_code_alter_products_item_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorproducts',
            name='delivery_fee',
            field=models.FloatField(default=0),
        ),
    ]
