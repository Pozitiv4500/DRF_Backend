# Generated by Django 4.2.7 on 2023-11-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_casino', '0007_alter_casinoprofile_interface_languages_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casinoprofile',
            name='interface_languages_image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='casinoprofile',
            name='payments_images',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='casinoprofile',
            name='providers_images',
            field=models.TextField(),
        ),
    ]