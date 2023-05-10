# Generated by Django 4.0.10 on 2023-05-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salsa_app', '0010_rename_moveshistory_movehistory_rename_moves_move_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='base_move',
            field=models.CharField(blank=True, choices=[('CrossBody', 'CrossBody'), ('Hamalock', 'Hamalock'), ('Kopa', 'Kopa'), ('OpenBreak', 'OpenBreak'), ('Titanic', 'Titanic')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='entry_hold',
            field=models.CharField(blank=True, choices=[('Left2Left', 'Left2Left'), ('Right2Right', 'Right2Right'), ('Right2Left', 'Right2Left'), ('Left2Right', 'Left2Right'), ('Both Normal Hold', 'Both Normal Hold'), ('Both - Left Over Right', 'Both - Left Over Right'), ('Both - Right Over Left', 'Both - Right Over Left')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='exit_hold',
            field=models.CharField(blank=True, choices=[('Left2Left', 'Left2Left'), ('Right2Right', 'Right2Right'), ('Right2Left', 'Right2Left'), ('Left2Right', 'Left2Right'), ('Both Normal Hold', 'Both Normal Hold'), ('Both - Left Over Right', 'Both - Left Over Right'), ('Both - Right Over Left', 'Both - Right Over Left')], max_length=40, null=True),
        ),
    ]
