# Generated by Django 4.2.7 on 2023-11-16 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_casino', '0005_remove_casinoprofile_interface_languages_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casinoprofile',
            name='interface_languages_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_casino.interfacelanguagesimage'),
        ),
        migrations.AlterField(
            model_name='casinoprofile',
            name='payments_images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_casino.paymentimage'),
        ),
        migrations.AlterField(
            model_name='casinoprofile',
            name='providers_images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_casino.providerimage'),
        ),
    ]
