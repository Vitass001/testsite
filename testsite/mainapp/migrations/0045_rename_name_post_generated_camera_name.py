# Generated by Django 3.2.7 on 2023-05-04 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0044_auto_20230504_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='Generated_Camera_name',
        ),
    ]
