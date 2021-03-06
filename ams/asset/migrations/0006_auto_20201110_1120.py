# Generated by Django 3.1.2 on 2020-11-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_auto_20201110_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='manufacturer_name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
