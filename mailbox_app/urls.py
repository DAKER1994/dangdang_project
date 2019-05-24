from django.contrib import admin
from django.urls import path
from mailbox_app import views

app_name = 'mailbox_app'
urlpatterns = [
    path('arrive_form/',views.arrive_form,name='arrive_form'),
    path('user_register/',views.user_register,name='user_register'),
    path('user_confirm/',views.user_confirm,name='user_confirm'),
]