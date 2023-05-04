# Generated by Django 3.2.7 on 2023-05-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0045_rename_name_post_generated_camera_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='customer_sme_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='door_sticker_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='leave_fw_install_crib_sheet_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='set_up_pc_and_app',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='train_staff',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='confirm_video_recorded',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='firmware_up_to_date',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sd_card_installed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='settings_optimized',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
