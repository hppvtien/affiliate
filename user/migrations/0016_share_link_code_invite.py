# Generated by Django 3.2.8 on 2021-10-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_share_link_share_link_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='share_link',
            name='code_invite',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
