# Generated by Django 4.2.7 on 2023-12-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_casino', '0019_alter_gameprofile_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamesOfWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id_1', models.PositiveIntegerField()),
                ('game_id_2', models.PositiveIntegerField()),
                ('game_id_3', models.PositiveIntegerField()),
            ],
        ),
    ]
