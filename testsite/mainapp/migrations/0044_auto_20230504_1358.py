# Generated by Django 3.2.7 on 2023-05-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0043_post_face_box_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='face_size_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='firmware_up_to_date',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='min_face_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sd_card_installed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='settings_optimized',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
