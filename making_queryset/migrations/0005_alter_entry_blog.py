# Generated by Django 3.2 on 2022-06-12 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('making_queryset', '0004_alter_entry_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='making_queryset.blog'),
        ),
    ]