# Generated by Django 4.0.10 on 2023-05-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salsa_app', '0011_alter_move_base_move_alter_move_entry_hold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='easiness_factor',
            field=models.FloatField(default=2.5),
        ),
        migrations.AddField(
            model_name='combo',
            name='interval',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='combo',
            name='repetition',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='combohistory',
            name='easiness_factor',
            field=models.FloatField(default=2.5),
        ),
        migrations.AddField(
            model_name='combohistory',
            name='interval',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='combohistory',
            name='repetition',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='move',
            name='easiness_factor',
            field=models.FloatField(default=2.5),
        ),
        migrations.AddField(
            model_name='move',
            name='interval',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='move',
            name='repetition',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movehistory',
            name='easiness_factor',
            field=models.FloatField(default=2.5),
        ),
        migrations.AddField(
            model_name='movehistory',
            name='interval',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movehistory',
            name='repetition',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='move',
            name='base_move',
            field=models.CharField(blank=True, choices=[('CrossBody-InsideTurn', 'CrossBody-InsideTurn'), ('CrossBody-OutsideTurn', 'CrossBody-OutsideTurn'), ('CrossBody', 'CrossBody'), ('InsideTurn', 'InsideTurn'), ('OutsideTurn', 'OutsideTurn'), ('Leader hammerlock', 'Leader hammerlock'), ('Follower hammerlock', 'Follower hammerlock'), ('Copa', 'Copa'), ('OpenBreak', 'OpenBreak'), ('Titanic', 'Titanic'), ('RightSidePass', 'RightSidePass'), ('BodyWrap', 'BodyWrap')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='entry_hold',
            field=models.CharField(blank=True, choices=[('Left2Left', 'Left2Left'), ('Right2Right', 'Right2Right'), ('Right2Left', 'Right2Left'), ('Left2Right', 'Left2Right'), ('ClosedPosition', 'ClosedPosition'), ('Both Normal Hold', 'Both Normal Hold'), ('Both - Left Over Right', 'Both - Left Over Right'), ('Both - Right Over Left', 'Both - Right Over Left'), ('Free Spin', 'Free Spin')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='exit_hold',
            field=models.CharField(blank=True, choices=[('Left2Left', 'Left2Left'), ('Right2Right', 'Right2Right'), ('Right2Left', 'Right2Left'), ('Left2Right', 'Left2Right'), ('ClosedPosition', 'ClosedPosition'), ('Both Normal Hold', 'Both Normal Hold'), ('Both - Left Over Right', 'Both - Left Over Right'), ('Both - Right Over Left', 'Both - Right Over Left'), ('Free Spin', 'Free Spin')], max_length=40, null=True),
        ),
    ]
