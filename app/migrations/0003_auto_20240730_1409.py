# Generated by Django 3.0.5 on 2024-07-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_studentreg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreg',
            name='birthdate',
            field=models.CharField(max_length=20),
        ),
    ]
