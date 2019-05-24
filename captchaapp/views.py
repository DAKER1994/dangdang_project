from django.shortcuts import render,HttpResponse
import random,string,os
from captchaapp.captcha.image import ImageCaptcha
# Create your views here.
def getcaptcha(request):
    image = ImageCaptcha()
    # image =ImageCaptcha(fonts=[os.path.abspath(("DroidSansMono.ttf"))])
    rand_code=random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,5)
    rand_code ="".join(rand_code)
    print(rand_code)
    request.session["code"] =rand_code
    data =image.generate(rand_code)
    return HttpResponse(data,"image/png")
def regist(request):
    return render(request,"captcha/register.html")

def registlogic(request):
    captcha =request.POST.get("captcha")
    code =request.session.get("code")
    if captcha.upper() == code.upper():
        return HttpResponse("验证码正确")
    else:
        return HttpResponse("验证码输入有误")



