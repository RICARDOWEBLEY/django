# Generated by Django 3.1.2 on 2020-11-10 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20201110_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='asset',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='asset.acquisition'),
        ),
    ]
