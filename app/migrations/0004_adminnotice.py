# Generated by Django 3.0.5 on 2024-07-31 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20240730_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
            ],
        ),
    ]
