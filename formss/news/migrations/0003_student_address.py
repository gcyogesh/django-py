# Generated by Django 4.2 on 2023-04-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default=1, max_length=130),
            preserve_default=False,
        ),
    ]