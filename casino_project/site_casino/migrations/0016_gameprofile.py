# Generated by Django 4.2.7 on 2023-12-19 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_casino', '0015_alter_casinoprofile_promo_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=100)),
                ('image_link', models.URLField()),
                ('ranking_position', models.PositiveIntegerField()),
                ('editor_rating', models.FloatField()),
                ('game_text', models.TextField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('min_bet', models.FloatField()),
                ('max_bet', models.FloatField()),
                ('max_payout', models.FloatField()),
                ('reels', models.PositiveIntegerField()),
                ('rows', models.PositiveIntegerField()),
                ('pay_lines', models.PositiveIntegerField()),
                ('rtp', models.FloatField()),
                ('volatility', models.CharField(max_length=50)),
                ('platforms', models.CharField(max_length=100)),
                ('casino_id_1', models.PositiveIntegerField()),
                ('casino_id_2', models.PositiveIntegerField()),
                ('multiple_casino_ids', models.TextField()),
            ],
        ),
    ]