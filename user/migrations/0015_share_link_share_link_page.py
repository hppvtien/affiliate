# Generated by Django 3.2.8 on 2021-10-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20211009_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='share_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField(unique=True)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='share_link_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('code', models.TextField()),
                ('page_link', models.TextField()),
                ('count_view_site', models.IntegerField()),
            ],
        ),
    ]