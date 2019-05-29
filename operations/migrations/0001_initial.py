# Generated by Django 2.2.dev20181212174947 on 2019-05-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('description', models.TextField(default='', max_length=500)),
                ('cover', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gist',
            fields=[
                ('id', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=500)),
                ('youTubeUrl', models.CharField(blank=True, default='', max_length=255)),
                ('content', models.TextField(default='', max_length=500)),
                ('summary', models.TextField(blank=True, default='', max_length=1000)),
                ('category', models.ManyToManyField(blank=True, to='operations.Category')),
                ('gistId', models.ManyToManyField(blank=True, to='operations.Gist')),
                ('tags', models.ManyToManyField(to='operations.Tag')),
            ],
        ),
    ]