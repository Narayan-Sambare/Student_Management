# Generated by Django 3.0.5 on 2024-07-31 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_adminnotice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminnotice',
            old_name='date',
            new_name='date1',
        ),
    ]
