# Generated by Django 4.2.6 on 2023-10-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='id',
            field=models.CharField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='buildingtype',
            name='name',
            field=models.CharField(default='BUILDING', unique=True),
        ),
    ]
