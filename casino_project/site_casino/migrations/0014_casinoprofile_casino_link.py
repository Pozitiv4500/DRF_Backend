# Generated by Django 4.2.7 on 2023-12-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_casino', '0013_casinoprofile_casino_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='casinoprofile',
            name='casino_link',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
