# Generated by Django 4.1.1 on 2022-09-28 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecourses', '0004_remove_tags_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='lessons',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags', to='ecourses.lessons'),
        ),
    ]
