# Generated by Django 2.2.dev20181212174947 on 2019-05-24 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_post_gistid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='gistId',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='Gist',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]