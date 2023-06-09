# Generated by Django 4.0.10 on 2023-05-06 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salsa_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='combohistory',
            name='date',
        ),
        migrations.RemoveField(
            model_name='moves',
            name='base_move',
        ),
        migrations.RemoveField(
            model_name='moveshistory',
            name='date',
        ),
        migrations.AddField(
            model_name='combohistory',
            name='date_last_practiced',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2000, 1, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='combohistory',
            name='date_last_practiced_social',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2000, 1, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='moves',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moves',
            name='video_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moveshistory',
            name='date_last_practiced',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2000, 1, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='moveshistory',
            name='date_last_practiced_social',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2000, 1, 1, 0, 0)),
        ),
    ]
