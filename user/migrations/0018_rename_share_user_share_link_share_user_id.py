# Generated by Django 3.2.8 on 2021-10-06 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_share_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='share_link',
            old_name='share_user',
            new_name='share_user_id',
        ),
    ]
