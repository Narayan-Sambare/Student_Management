# Generated by Django 3.0.5 on 2024-07-31 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20240731_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminnotice',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]