# Generated by Django 4.2 on 2023-04-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwd_manager_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
