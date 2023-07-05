# Generated by Django 4.0 on 2023-06-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='what_we_do',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=50)),
                ('link_name', models.CharField(max_length=50)),
                ('paragraph', models.TextField()),
            ],
        ),
    ]