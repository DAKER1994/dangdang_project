from django.contrib import admin
from django.urls import path
from xmapp import views
app_name ='xmapp'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('details/',views.details,name='details'),
    path('regist/',views.regist,name='regist'),
    path('regist_ok/',views.regist_ok,name='regist_ok'),
    path('booklist/',views.booklist,name='booklist'),
    path('car/',views.car,name='car'),
    path('indent/',views.indent,name='indent'),
    path('indentok/',views.indent_ok,name='indentok'),
    path('login/',views.login,name='login'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('registlogic/',views.regist_logic,name='registlogic'),
    path('checkname/',views.checkemail,name='checkemail'),
    path('checknum/',views.checknum,name='checknum'),
    path('checkpwd/',views.checkpwd,name='checkpwd'),
    path('checklogincode/',views.checklogincode,name='checklogincode'),
    path('logout/',views.logout,name='logout'),
    path('addbook/',views.add_book,name='addbook'),
    path('del_book_info/',views.del_book_info,name='del_book_info'),
    path('indentajax1/',views.indent_ajax1,name='indentajax1'),

]