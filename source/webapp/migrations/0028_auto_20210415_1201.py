# Generated by Django 2.2 on 2021-04-15 06:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0027_auto_20210415_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.AddField(
            model_name='project',
            name='project_team',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Команда'),
        ),
        migrations.AddField(
            model_name='tipe',
            name='tipe_team',
            field=models.ManyToManyField(related_name='tipes', to=settings.AUTH_USER_MODEL, verbose_name='Команда'),
        ),
    ]
