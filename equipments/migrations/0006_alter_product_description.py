# Generated by Django 4.1.2 on 2022-10-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0005_product_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
    ]
