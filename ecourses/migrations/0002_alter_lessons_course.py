# Generated by Django 4.1.1 on 2022-09-28 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecourses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='ecourses.courses'),
        ),
    ]
