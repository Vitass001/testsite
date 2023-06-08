from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    # path('product/', product_list, name='product_list'),
    path('create/', post_create, name='post_create'),
    path('detail/', post_detail, name='post_detail'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/', post_detail_old, name='post_detail_old'),
    path('create_property/', create_property, name='create_property'),
    path('create_Legal_Entity/', create_Legal_Entity, name='create_Legal_Entity'),

    path('posts/', all_posts, name='all_posts'),
    path('posts/calculator/', calculator, name='calculator'),

    # path('<str:legal_Entity>/<str:property>/<str:Camera_Name>/', post_detail, name='post_detail'),
    path('detail/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/', post_detail, name='post_detail'),

    path('property_list_ajax/', property_list_ajax, name='property_list_ajax'),



    path('detail/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit/', post_edit, name='post_edit'),
    path('detail/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit0/', post_edit0, name='post_edit0'),
    path('detail/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit1/', post_edit1, name='post_edit1'),
    path('detail/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit2/', post_edit2, name='post_edit2'),
    path('detail/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit3/', post_edit3, name='post_edit3'),
    path('detail/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit4/', post_edit4, name='post_edit4'),
    path('detail/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/delete/', post_delete, name='post_delete'),



    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings0/', post_edit_Settings0, name='post_edit_Settings0'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings1/', post_edit_Settings1, name='post_edit_Settings1'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings2/', post_edit_Settings2, name='post_edit_Settings2'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings3/', post_edit_Settings3, name='post_edit_Settings3'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings4/', post_edit_Settings4, name='post_edit_Settings4'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings5/', post_edit_Settings5, name='post_edit_Settings5'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings6/', post_edit_Settings6, name='post_edit_Settings6'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings7/', post_edit_Settings7, name='post_edit_Settings7'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings8/', post_edit_Settings8, name='post_edit_Settings8'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings9/', post_edit_Settings9, name='post_edit_Settings9'),
    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/settings10/', post_edit_Settings10, name='post_edit_Settings10'),

    path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/', post_detail_old, name='post_detail_old'),
    # path('detail_old/<str:Legal_Entity>-<str:property>-<str:Camera_Name>/delete/', post_delete, name='post_delete'),
    # path('<str:title>/delete1/', post_delete1, name='post_delete1'),
    # path('<str:title>/delete2/', post_delete2, name='post_delete2'),
    path('posts/search/', search, name='search'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('list/', book_author_list, name='book_author_list'),



    # path('update/', update_post, name='update_post'),
]
