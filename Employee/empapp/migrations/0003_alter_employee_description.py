# Generated by Django 5.0.1 on 2024-03-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_employee_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]