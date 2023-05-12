# Generated by Django 4.0.10 on 2023-05-12 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salsa_app', '0019_remove_move_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='date_next_review',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2000, 1, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='position',
            name='difficulty_remembering',
            field=models.CharField(choices=[('3', 'Easy'), ('2', 'Good'), ('1', 'Again')], default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='position',
            name='easiness_factor_remembering',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='interval',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='repetition',
            field=models.IntegerField(default=0),
        ),
    ]
