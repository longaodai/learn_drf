# Generated by Django 4.1.1 on 2022-09-28 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecourses', '0003_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='lessons',
        ),
    ]
