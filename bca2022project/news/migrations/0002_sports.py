# Generated by Django 4.1.7 on 2023-04-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('page_views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
