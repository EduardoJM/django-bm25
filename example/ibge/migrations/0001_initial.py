# Generated by Django 4.2.6 on 2023-10-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('state', models.CharField(max_length=2, verbose_name='State')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
    ]