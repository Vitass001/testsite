from django import forms
from django.core.exceptions import ValidationError

from .models import Post
from .models import *
from .models import Post
from .models import Property


class LegalForm(forms.ModelForm):

    class Meta:
        model = Legal
        fields = ['Legal_Entity']


class PropertyForm(forms.ModelForm):
    Legal_Entity = forms.ModelChoiceField(queryset=Legal.objects.values_list('Legal_Entity', flat=True).distinct(),
                                          to_field_name='Legal_Entity')

    class Meta:
        model = Property
        fields = ['Legal_Entity', 'property', 'town', 'postcode', 'phone_number']


class PostForm(forms.ModelForm):
    # company = forms.ModelChoiceField(queryset=Property.objects.values_list('company', flat=True).distinct())
    Legal_Entity = forms.ModelChoiceField(queryset=Property.objects.values_list('Legal_Entity', flat=True).distinct(),
                                     to_field_name='Legal_Entity')
    property = forms.ModelChoiceField(queryset=Property.objects.values_list('property', flat=True).distinct(),
                                     to_field_name='property')


    class Meta:
        model = Post

        fields = ['Legal_Entity', 'property', 'Camera_Name',
                   ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Legal_Entity'].queryset = Property.objects.values_list('Legal_Entity', flat=True).distinct()

        if 'Legal_Entity' in self.data:
            try:
                legal_entity = self.data.get('Legal_Entity')
                self.fields['property'].queryset = Property.objects.filter(Legal_Entity=legal_entity).values_list(
                    'property', flat=True).distinct()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['property'].queryset = Property.objects.filter(
                Legal_Entity=self.instance.Legal_Entity).values_list('property', flat=True).distinct()

    def clean(self):
        cleaned_data = super().clean()
        legal_entity = cleaned_data.get("Legal_Entity")
        property = cleaned_data.get("property")
        camera_name = cleaned_data.get("Camera_Name")

        if Post.objects.filter(Legal_Entity=legal_entity, property=property, Camera_Name=camera_name).exists():
            raise ValidationError("A camera with these values already exists")

        return cleaned_data


class PostForm0(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['town', 'postcode', 'phone_number', 'confirm_video_recorded', 'door_photo', 'aspect_of_door', 'light_meter_reading_inside',
                   'internet_speed_test']






class PostForm1(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['camera_serial', 'face_box_id', 'kasa_login_id', 'switch_make_and_model', 'router_serial', 'phone_models', 'phone_serial', 'phone_sim',
                  'Photo_of_camera', 'Photo_of_router', 'Photo_of_switch']
        # fields = ['Installer_Company', 'Installer_email', 'Install_date', 'Door_entrance_width',
        #         'Distance_from_door', 'Height', 'Angle_to_face_Degrees', 'Pixels_per_face',
        #         'Video_on_teams', 'Facebox_id', 'Kasa_login', 'Router_Serial_No',
        #         'Phone_Model', 'Phone_Serial_No', 'Lightmeter_reading_at_entrance']

        # widgets = {
        #     'category': forms.Select(choices=Post.CATEGORY_CHOICES)
        # }

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Generated_Camera_name', 'firmware_up_to_date', 'sd_card_installed', 'settings_optimized', 'face_size_screenshot',
                  'min_face_size', 'notes']

        # fields = ['Vivotek_cam_updated', 'Lumen_or_candle', 'Auto_Camera_Name',
        #           'Input_Camera_Name_Into_Camera', 'Aspect', 'Door_type', 'Describe_aspect',
        #           'Camera_time', 'Bitrate', 'Video_quality', 'Zoom_to_door_and_preset']


class PostForm3(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['door_sticker_photo', 'set_up_pc_and_app', 'train_staff', 'customer_sme_name', 'leave_fw_install_crib_sheet_photo']
        # fields = ['Horiz_mfs_from_detection', 'Horiz_mfs_from_safr', 'Are_faces_detected',
        #           'Are_alerts_working', 'Name_of_store_manager', 'Is_web_login', 'User_login_app',
        #           'User_trained', 'Name_of_fw_user']


class PostForm4(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Camera_Position_Image', 'Facebox_Switch_location_image', 'Router_location_image', 'Image_of_signage_in_doorway_image'
                   ]
        widgets = {
            'Camera_Position_Image': forms.FileInput(attrs={'multiple': True}),
            ' Facebox_Switch_location_image': forms.FileInput(attrs={'multiple': True}),

            'Router_location_image': forms.FileInput(attrs={'multiple': True}),
            'Image_of_signage_in_doorway_image': forms.FileInput(attrs={'multiple': True}),
        }









class PostForm_Settings0(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Legal_Entity', 'Property_Name', 'Town_Postcode', 'Camera_Name', 'Company'
                   ]

        # widgets = {
        #     'category': forms.Select(choices=Post.CATEGORY_CHOICES)
        # }

class PostForm_Settings1(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Installer_Company', 'Installer_email', 'Install_date', 'Door_entrance_width',
                'Distance_from_door', 'Height', 'Angle_to_face_Degrees', 'Pixels_per_face',
                'Video_on_teams', 'Facebox_id', 'Kasa_login', 'Router_Serial_No',
                'Phone_Model', 'Phone_Serial_No', 'Lightmeter_reading_at_entrance']

        # widgets = {
        #     'category': forms.Select(choices=Post.CATEGORY_CHOICES)
        # }

class PostForm_Settings2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Vivotek_cam_updated', 'Lumen_or_candle', 'Auto_Camera_Name',
                  'Input_Camera_Name_Into_Camera', 'Aspect', 'Door_type', 'Describe_aspect',
                  'Camera_time', 'Bitrate', 'Video_quality', 'Zoom_to_door_and_preset']
        # widgets = {
        #     'Camera_position_photo': forms.ClearableFileInput(attrs={'multiple': True}),
        #     'Facebox_photo': forms.ClearableFileInput(attrs={'multiple': True}),
        #     'Switch_photo': forms.ClearableFileInput(attrs={'multiple': True}),
        #     'Router_photo': forms.ClearableFileInput(attrs={'multiple': True}),
        # }

        # widgets = {
        #     'category': forms.Select(choices=Post.CATEGORY_CHOICES)
        # }


class PostForm_Settings3(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Horiz_mfs_from_detection', 'Horiz_mfs_from_safr', 'Are_faces_detected',
                  'Are_alerts_working', 'Name_of_store_manager', 'Is_web_login', 'User_login_app',
                  'User_trained', 'Name_of_fw_user']



class PostForm_Settings4(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Camera_Position_Image', 'Facebox_Switch_location_image', 'Router_location_image', 'Image_of_signage_in_doorway_image'
                   ]
        widgets = {
            'Camera_Position_Image': forms.ClearableFileInput(attrs={'multiple': True}),
            ' Facebox_Switch_location_image': forms.ClearableFileInput(attrs={'multiple': True}),

            'Router_location_image': forms.ClearableFileInput(attrs={'multiple': True}),
            'Image_of_signage_in_doorway_image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class PostForm_Settings5(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Safr_feed_name', 'Safr_feed_site', 'Safr_feed_source', 'Rtsp_adress',
                  'Safr_mfs', 'Safr_tracker_failed', 'Safr_min_pose_quality', 'Safr_min_backoff'
                   ]

class PostForm_Settings6(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Camera_serial_no', 'Name_of_profile_day', 'Time_profile_day',
                  'White_balance_day', 'Brightness_day', 'Saturation_day', 'Sharpness_day',
                  'Digital_noise_day', 'Exposure_level_day', 'Exposure_mode_day', 'Iris_day',
                  'Exposure_gain_day', 'Exposure_time_day', 'Wdr_pro_day', 'wdr_level_day'
                   ]
class PostForm_Settings7(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Name_of_profile_night', 'Time_profile_night', 'White_balance_night',
                  'Brightness_night', 'Saturation_night', 'Sharpness_night', 'Digital_noise_night',
                  'Exposure_level_night', 'Exposure_mode_night', 'Iris_night', 'Exposure_time_night',
                  'Exposure_gain_night', 'Wdr_pro_night', 'wdr_level_night']


class PostForm_Settings8(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Name_of_profile_one', 'Time_profile_one', 'White_balance_one', 'Brightness_one',
                  'Saturation_one', 'Sharpness_one', 'Digital_noise_one', 'Exposure_level_one',
                  'Exposure_mode_one', 'Iris_one', 'Exposure_time_one', 'Exposure_gain_one',
                  'Wdr_pro_one', 'wdr_level_one']



class PostForm_Settings9(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Name_of_profile_two', 'Time_profile_two', 'White_balance_two',
                  'Brightness_two', 'Saturation_two', 'Sharpness_two', 'Digital_noise_two',
                  'Exposure_level_two', 'Exposure_mode_two', 'Iris_two', 'Exposure_time_two',
                  'Exposure_gain_two', 'Wdr_pro_two', 'wdr_level_two']
class PostForm_Settings10(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['field_for_notes',
                   ]





class LoginForm(forms.Form):
    # email = forms.EmailField()
    # username = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autofocus': True}))
    username = forms.CharField(label='Login', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')



