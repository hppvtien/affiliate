# Generated by Django 3.2.7 on 2021-09-22 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_profile_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='district',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='province',
        ),
    ]
