# Generated by Django 4.1.1 on 2022-10-03 10:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battle', '0002_alter_game_battle_map_alter_game_finished_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='step_counter',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='spectators',
            field=models.ManyToManyField(blank=True, related_name='viewed_game', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='signed_game', to=settings.AUTH_USER_MODEL),
        ),
    ]
