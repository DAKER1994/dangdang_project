from django.urls import path
# from captchapp.models import
from captchaapp import views
app_name ="captcha"
urlpatterns =[
    path("getcaptcha/",views.getcaptcha,name="getcaptcha"),
    path("regist/",views.regist,name="regist"),
    path("registlogic/",views.registlogic,name="registlogic"),
]