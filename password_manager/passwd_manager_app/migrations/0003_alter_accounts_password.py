# Generated by Django 4.2 on 2023-04-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwd_manager_app', '0002_alter_accounts_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]