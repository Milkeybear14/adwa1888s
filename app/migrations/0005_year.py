# Generated by Django 4.1.7 on 2023-06-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_clients_response_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4)),
            ],
        ),
    ]
