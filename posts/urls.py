from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('',views.hello, name='hello'),
    path('getarea/',views.getarea),
    # path('post/<int:post_id>',views.show_post, name='post'),
    # path('post/<slug:post_slug>',views.show_post, name='post'),
    path('send/',send_message),
    path('registration/',views.registration,name='registration'),
    path('show_post',views.show_post,name='show_post')
]