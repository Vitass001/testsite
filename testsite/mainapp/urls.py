from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    # path('product/', product_list, name='product_list'),
    path('create/', post_create, name='post_create'),
    path('detail/', post_detail, name='post_detail'),
    path('create_property/', create_property, name='create_property'),
    path('create_Legal_Entity/', create_Legal_Entity, name='create_Legal_Entity'),

    path('posts/', all_posts, name='all_posts'),
    path('posts/calculator/', calculator, name='calculator'),

    # path('<str:legal_Entity>/<str:property>/<str:Camera_Name>/', post_detail, name='post_detail'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/', post_detail, name='post_detail'),

    path('property_list_ajax/', property_list_ajax, name='property_list_ajax'),



    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit/', post_edit, name='post_edit'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit0/', post_edit0, name='post_edit0'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit1/', post_edit1, name='post_edit1'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit2/', post_edit2, name='post_edit2'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit3/', post_edit3, name='post_edit3'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit4/', post_edit4, name='post_edit4'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit5/', post_edit5, name='post_edit5'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit6/', post_edit6, name='post_edit6'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit7/', post_edit7, name='post_edit7'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit8/', post_edit8, name='post_edit8'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit9/', post_edit9, name='post_edit9'),
    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/edit10/', post_edit10, name='post_edit10'),

    path('<str:Legal_Entity>-<str:property>-<str:Camera_Name>/delete/', post_delete, name='post_delete'),
    # path('<str:title>/delete1/', post_delete1, name='post_delete1'),
    # path('<str:title>/delete2/', post_delete2, name='post_delete2'),
    path('posts/search/', search, name='search'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('list/', book_author_list, name='book_author_list'),



    # path('update/', update_post, name='update_post'),
]
