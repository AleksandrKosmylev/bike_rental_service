# Generated by Django 5.0.7 on 2024-07-17 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Labels',
            new_name='Bikes',
        ),
    ]