# Generated by Django 4.2.7 on 2023-12-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_casino', '0012_alter_casinocomment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='casinoprofile',
            name='casino_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='casinoprofile',
            name='sorting_criteria',
            field=models.TextField(default=312),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='casinoprofile',
            name='player_rating',
            field=models.FloatField(default=5.0),
        ),
    ]
