from django.db import models

def upload_location(instance, filename):
    return f'{instance.id}, {filename}'

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Post(models.Model):

    # title = models.CharField(max_length=500,blank=True, null=True )
    #Create post
    Legal_Entity = models.CharField(max_length=500,)
    property = models.CharField(max_length=500, unique=True)
    Camera_Name = models.CharField(max_length=500,)
    Property_Name = models.CharField(max_length=500,blank=True, null=True )
    # Town_Postcode = models.CharField(max_length=500,blank=True, null=True )
    town = models.CharField(max_length=500, )
    postcode = models.CharField(max_length=500, )
    phone_number = models.CharField(max_length=500, )
    # Test_admin = models.CharField(max_length=500, unique=True)
    confirm_video_recorded = models.BooleanField(default=False,blank=True, null=True)
    door_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    aspect_of_door = models.CharField(blank=True, null=True, max_length=500)
    light_meter_reading_inside = models.CharField(blank=True, null=True, max_length=500)
    # калькулятор
    # camera_calculator_info = models.CharField(blank=True, null=True, max_length=500)

    internet_speed_test = models.ImageField(upload_to='images/', blank=True, null=True)







    # Install on site
    Installer_Company = models.CharField(max_length=500,blank=True, null=True )
    Installer_email = models.CharField(max_length=500,blank=True, null=True )
    Install_date = models.CharField(max_length=500, blank=True, null=True)
    Door_entrance_width = models.CharField(max_length=500, blank=True, null=True)
    Distance_from_door= models.CharField(max_length=500, blank=True, null=True)
    Height = models.CharField(max_length=500, blank=True, null=True)
    Angle_to_face_Degrees = models.CharField(max_length=500, blank=True, null=True)
    Pixels_per_face = models.CharField(max_length=500, blank=True, null=True)
    Video_on_teams = models.CharField(max_length=500, blank=True, null=True)
    Facebox_id = models.CharField(max_length=500,blank=True, null=True )
    Kasa_login = models.CharField(max_length=500,blank=True, null=True )
    Router_Serial_No = models.CharField(max_length=500, blank=True, null=True)
    Phone_Model = models.CharField(max_length=500, blank=True, null=True)
    Phone_Serial_No = models.CharField(max_length=500, blank=True, null=True)
    Lightmeter_reading_at_entrance = models.CharField(max_length=500, blank=True, null=True)


    Test_camera_set = models.CharField(max_length=500, blank=True, null=True)


#    INSTALER ON SITE
    Vivotek_cam_updated = models.CharField(max_length=500, blank=True, null=True)
    Lumen_or_candle = models.CharField(max_length=500, blank=True, null=True)
    Auto_Camera_Name = models.CharField(max_length=500,blank=True, null=True )
    Input_Camera_Name_Into_Camera = models.CharField(max_length=500, blank=True, null=True)
    Aspect = models.CharField(max_length=500,blank=True, null=True )
    Door_type = models.CharField(max_length=500, blank=True, null=True)
    Describe_aspect = models.CharField(max_length=500,blank=True, null=True )
    Camera_time = models.CharField(max_length=500,blank=True, null=True )
    Bitrate = models.CharField(max_length=500,blank=True, null=True )
    Video_quality = models.CharField(max_length=500,blank=True, null=True )
    Zoom_to_door_and_preset= models.CharField(max_length=500, blank=True, null=True)

    #Final checks
    Horiz_mfs_from_detection = models.CharField(max_length=500, blank=True, null=True)
    Horiz_mfs_from_safr = models.CharField(max_length=500, blank=True, null=True)
    Are_faces_detected = models.CharField(max_length=500, blank=True, null=True)
    Are_alerts_working = models.CharField(max_length=500, blank=True, null=True)
    Name_of_store_manager = models.CharField(max_length=500, blank=True, null=True)
    Is_web_login = models.CharField(max_length=500, blank=True, null=True)
    User_login_app = models.CharField(max_length=500, blank=True, null=True)
    User_trained = models.CharField(max_length=500, blank=True, null=True)
    Name_of_fw_user = models.CharField(max_length=500, blank=True, null=True)


    #Safr info
    Safr_feed_name = models.CharField(max_length=500, blank=True, null=True)
    Safr_feed_site = models.CharField(max_length=500, blank=True, null=True)
    Safr_feed_source = models.CharField(max_length=500, blank=True, null=True)
    Rtsp_adress= models.CharField(max_length=500, blank=True, null=True)
    Safr_mfs = models.CharField(max_length=500, blank=True, null=True)
    Safr_min_backoff = models.CharField(max_length=500, blank=True, null=True)
    Safr_tracker_failed = models.CharField(max_length=500, blank=True, null=True)
    Safr_min_pose_quality = models.CharField(max_length=500, blank=True, null=True)



    #Photos
    Camera_Position_Image = models.ImageField(upload_to='images/',
                                              null=True, blank=True,)
    Facebox_Switch_location_image = models.ImageField(upload_to='images/',
                               null=True, blank=True,)
    Router_location_image = models.ImageField(upload_to='images/',
                               null=True, blank=True,)
    Image_of_signage_in_doorway_image = models.ImageField(upload_to='images/',
                               null=True, blank=True,)

    # 'mainapp/static/mainapp/images/'
    #Day param
    Camera_serial_no = models.CharField(max_length=500, blank=True, null=True)
    Name_of_profile_day = models.CharField(max_length=500, blank=True, null=True)
    Time_profile_day = models.CharField(max_length=500, blank=True, null=True)
    White_balance_day = models.CharField(max_length=500, blank=True, null=True)
    Brightness_day = models.CharField(max_length=500, blank=True, null=True)
    Saturation_day = models.CharField(max_length=500, blank=True, null=True)
    Sharpness_day = models.CharField(max_length=500, blank=True, null=True)
    Digital_noise_day = models.CharField(max_length=500, blank=True, null=True)
    Exposure_level_day = models.CharField(max_length=500, blank=True, null=True)
    Exposure_mode_day = models.CharField(max_length=500, blank=True, null=True)
    Iris_day = models.CharField(max_length=500, blank=True, null=True)
    Exposure_time_day = models.CharField(max_length=500, blank=True, null=True)
    Exposure_gain_day = models.CharField(max_length=500, blank=True, null=True)
    Wdr_pro_day = models.CharField(max_length=500, blank=True, null=True)
    wdr_level_day = models.CharField(max_length=500, blank=True, null=True)

    Name_of_profile_night = models.CharField(max_length=500, blank=True, null=True)
    Time_profile_night = models.CharField(max_length=500, blank=True, null=True)
    White_balance_night = models.CharField(max_length=500, blank=True, null=True)
    Brightness_night = models.CharField(max_length=500, blank=True, null=True)
    Saturation_night = models.CharField(max_length=500, blank=True, null=True)
    Sharpness_night = models.CharField(max_length=500, blank=True, null=True)
    Digital_noise_night = models.CharField(max_length=500, blank=True, null=True)
    Exposure_level_night = models.CharField(max_length=500, blank=True, null=True)
    Exposure_mode_night = models.CharField(max_length=500, blank=True, null=True)
    Iris_night = models.CharField(max_length=500, blank=True, null=True)
    Exposure_time_night = models.CharField(max_length=500, blank=True, null=True)
    Exposure_gain_night = models.CharField(max_length=500, blank=True, null=True)
    Wdr_pro_night = models.CharField(max_length=500, blank=True, null=True)
    wdr_level_night = models.CharField(max_length=500, blank=True, null=True)

    Name_of_profile_one = models.CharField(max_length=500, blank=True, null=True)
    Time_profile_one = models.CharField(max_length=500, blank=True, null=True)
    White_balance_one = models.CharField(max_length=500, blank=True, null=True)
    Brightness_one = models.CharField(max_length=500, blank=True, null=True)
    Saturation_one = models.CharField(max_length=500, blank=True, null=True)
    Sharpness_one = models.CharField(max_length=500, blank=True, null=True)
    Digital_noise_one = models.CharField(max_length=500, blank=True, null=True)
    Exposure_level_one = models.CharField(max_length=500, blank=True, null=True)
    Exposure_mode_one = models.CharField(max_length=500, blank=True, null=True)
    Iris_one = models.CharField(max_length=500, blank=True, null=True)
    Exposure_time_one = models.CharField(max_length=500, blank=True, null=True)
    Exposure_gain_one = models.CharField(max_length=500, blank=True, null=True)
    Wdr_pro_one = models.CharField(max_length=500, blank=True, null=True)
    wdr_level_one = models.CharField(max_length=500, blank=True, null=True)

    Name_of_profile_two = models.CharField(max_length=500, blank=True, null=True)
    Time_profile_two = models.CharField(max_length=500, blank=True, null=True)
    White_balance_two = models.CharField(max_length=500, blank=True, null=True)
    Brightness_two = models.CharField(max_length=500, blank=True, null=True)
    Saturation_two = models.CharField(max_length=500, blank=True, null=True)
    Sharpness_two = models.CharField(max_length=500, blank=True, null=True)
    Digital_noise_two = models.CharField(max_length=500, blank=True, null=True)
    Exposure_level_two = models.CharField(max_length=500, blank=True, null=True)
    Exposure_mode_two = models.CharField(max_length=500, blank=True, null=True)
    Iris_two = models.CharField(max_length=500, blank=True, null=True)
    Exposure_time_two = models.CharField(max_length=500, blank=True, null=True)
    Exposure_gain_two = models.CharField(max_length=500, blank=True, null=True)
    Wdr_pro_two = models.CharField(max_length=500, blank=True, null=True)
    wdr_level_two = models.CharField(max_length=500, blank=True, null=True)

    field_for_notes = models.TextField(max_length=2000, blank=True, null=True)









    people_missing_check = models.CharField(max_length=500, blank=True, null=True)







    Test_safr = models.CharField(max_length=500,blank=True, null=True )
    Test_parametrs = models.CharField(max_length=500,blank=True, null=True )
    Test_extra1 = models.CharField(max_length=500,blank=True, null=True )
    Test_extra2 = models.CharField(max_length=500,blank=True, null=True )
    Test_night = models.CharField(max_length=500,blank=True, null=True )
    Test_notes = models.CharField(max_length=500,blank=True, null=True )



    # Entrance_signage = models.CharField(max_length=500, blank=True, null=True)
    # Confirm_all_working = models.CharField(max_length=500, blank=True, null=True)
    # User_who_was_trained = models.CharField(max_length=500, blank=True, null=True)
    # Camera_info = models.CharField(max_length=500, blank=True, null=True)
    #
    #
    #
    #
    #
    #
    #
    # door_with = models.IntegerField(max_length=500,blank=True, null=True )
    # camera_height = models.IntegerField(max_length=500,blank=True, null=True )
    # distance_to_door = models.IntegerField(max_length=500,blank=True, null=True )
    # zoom_perc = models.IntegerField(max_length=500, blank=True, null=True)




    pub_date = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to=upload_location,
    #                           null=True, blank=True,
    #                           height_field='height_field',
    #                           width_field='width_field',
    #                           )


    # image = models.ImageField(upload_to='mainapp/static/mainapp/images/',
    #                           null=True, blank=True,

                              # )
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
class Property(models.Model):
    Legal_Entity = models.CharField(max_length=500,)
    # company = models.CharField(max_length=500)
    property = models.CharField(max_length=500, unique=True)
    town = models.CharField(max_length=500,)
    postcode = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms.models import model_to_dict

@receiver(post_save, sender=Post)
def update_post(sender, instance, created, **kwargs):
    if created:  # перевіряємо, чи був створений новий об'єкт Post
        try:
            # знаходимо об'єкт Property, який відповідає вибраним значенням в PostForm
            property_obj = Property.objects.get(
                Legal_Entity=instance.Legal_Entity,
                property=instance.property
            )
            # отримуємо словник зі значеннями полів об'єкта Property та оновлюємо поля об'єкта Post
            post_dict = model_to_dict(property_obj, fields=['town', 'postcode', 'phone_number'])
            for key, value in post_dict.items():
                setattr(instance, key, value)
            instance.save()
        except Property.DoesNotExist:
            pass