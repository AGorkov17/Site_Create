# Generated by Django 4.2 on 2023-05-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Никнэйм')),
                ('vol_1', models.FloatField(verbose_name='Алкоголь')),
                ('vol_2', models.FloatField(verbose_name='Другие напитки')),
            ],
        ),
    ]