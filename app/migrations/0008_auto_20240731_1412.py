# Generated by Django 3.0.5 on 2024-07-31 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20240731_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminnotice',
            name='ndate1',
            field=models.DateField(),
        ),
    ]
