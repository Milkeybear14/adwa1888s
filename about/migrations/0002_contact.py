# Generated by Django 4.0 on 2023-06-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
