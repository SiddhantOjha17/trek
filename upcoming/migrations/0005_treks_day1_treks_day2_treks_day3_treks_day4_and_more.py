# Generated by Django 4.1.2 on 2022-10-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upcoming', '0004_treks_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='treks',
            name='day1',
            field=models.CharField(blank=True, default=False, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='treks',
            name='day2',
            field=models.CharField(blank=True, default=False, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='treks',
            name='day3',
            field=models.CharField(blank=True, default=False, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='treks',
            name='day4',
            field=models.CharField(blank=True, default=False, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='treks',
            name='day5',
            field=models.CharField(blank=True, default=False, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='treks',
            name='day6',
            field=models.CharField(blank=True, default=False, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='treks',
            name='long_description',
            field=models.CharField(default=False, max_length=1000),
        ),
    ]
