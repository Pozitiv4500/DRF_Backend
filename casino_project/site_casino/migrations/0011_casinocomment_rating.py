# Generated by Django 4.2.7 on 2023-11-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_casino', '0010_alter_casinocomment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='casinocomment',
            name='rating',
            field=models.PositiveIntegerField(default=4.8),
            preserve_default=False,
        ),
    ]
