# Generated by Django 4.2 on 2023-05-09 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='vol_2',
            new_name='non',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='vol_1',
            new_name='vol',
        ),
    ]