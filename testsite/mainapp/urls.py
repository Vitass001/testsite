from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views
from .views import *

urlpatterns = [
    path('', home_page,),
    # path('product/', product_list, name='product_list'),
    path('create/', post_create, name='post_create'),
    path('detail/', post_detail, name='post_detail'),
    path('posts/', all_posts, name='all_posts'),
    path('posts/calculator/', calculator, name='calculator'),
    path('<str:Legal_Entity>/', post_detail, name='post_detail'),

    path('<str:Legal_Entity>/edit/', post_edit, name='post_edit'),
    path('<str:Legal_Entity>/edit1/', post_edit1, name='post_edit1'),
    path('<str:Legal_Entity>/edit2/', post_edit2, name='post_edit2'),
    path('<str:Legal_Entity>/edit3/', post_edit3, name='post_edit3'),
    path('<str:Legal_Entity>/edit4/', post_edit4, name='post_edit4'),
    path('<str:Legal_Entity>/edit5/', post_edit5, name='post_edit5'),
    path('<str:Legal_Entity>/edit6/', post_edit6, name='post_edit6'),
    path('<str:Legal_Entity>/edit7/', post_edit7, name='post_edit7'),
    path('<str:Legal_Entity>/edit8/', post_edit8, name='post_edit8'),
    path('<str:Legal_Entity>/edit9/', post_edit9, name='post_edit9'),
    path('<str:Legal_Entity>/edit10/', post_edit10, name='post_edit10'),

    path('<str:Legal_Entity>/delete/', post_delete, name='post_delete'),
    # path('<str:title>/delete1/', post_delete1, name='post_delete1'),
    # path('<str:title>/delete2/', post_delete2, name='post_delete2'),
    path('posts/search/', search, name='search'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('list/', book_author_list, name='book_author_list'),



    # path('update/', update_post, name='update_post'),
]
