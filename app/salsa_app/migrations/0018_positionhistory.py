# Generated by Django 4.0.10 on 2023-05-11 16:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salsa_app', '0017_remove_move_base_move_alter_combo_difficulty_of_move_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_last_practiced', models.DateTimeField(blank=True, default=datetime.datetime(2000, 1, 1, 0, 0))),
                ('date_last_practiced_social', models.DateTimeField(blank=True, default=datetime.datetime(2000, 1, 1, 0, 0))),
                ('date_next_review', models.DateTimeField(blank=True, default=datetime.datetime(2000, 1, 1, 0, 0))),
                ('difficulty_remembering', models.CharField(choices=[('3', 'Easy'), ('2', 'Good'), ('1', 'Again')], default=0, max_length=20)),
                ('easiness_factor_remembering', models.IntegerField(default=0)),
                ('difficulty_of_move', models.CharField(choices=[('5', 'Can always do in socials'), ('4', 'Can sometimes do in socials'), ('3', 'Cant do in socials but can do in class'), ('4', 'Cant do in class'), ('5', 'Never Tried')], default=0, max_length=20)),
                ('repetition', models.IntegerField(default=0)),
                ('interval', models.IntegerField(default=0)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salsa_app.position')),
            ],
        ),
    ]
