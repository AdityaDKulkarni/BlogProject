# Generated by Django 2.2.dev20181212174947 on 2019-05-19 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='gistId',
        ),
    ]