# Generated by Django 3.2 on 2022-06-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image_url', models.CharField(max_length=100)),
            ],
        ),
    ]
