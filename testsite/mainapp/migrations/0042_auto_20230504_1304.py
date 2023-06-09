# Generated by Django 3.2.7 on 2023-05-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0041_auto_20230504_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='camera_serial',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='kasa_login_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='phone_models',
            field=models.CharField(blank=True, choices=[('Iphone 8 ', 'Iphone 8 '), ('Iphone 10', 'Iphone 10')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='phone_serial',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='phone_sim',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='router_serial',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='switch_make_and_model',
            field=models.CharField(blank=True, choices=[('HIK', 'HIK'), ('TPLink', 'TPLink')], max_length=50, null=True),
        ),
    ]
