# Generated by Django 4.2 on 2023-04-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_student_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]