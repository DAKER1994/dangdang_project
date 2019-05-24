from datetime import datetime
import hashlib
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render,HttpResponse

# Create your views here.
from mailbox_app import models


def arrive_form(request):
    return render(request,'mailbox_app/regist.html')


def hash_code(username, now):
    h = hashlib.md5()
    username += now
    h.update(username.encode())
    return h.hexdigest()


def make_confirm_string(new_user):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = hash_code(new_user.username,now)
    models.confirm_string.objects.create(code=code,user=new_user)
    return code


def send_email(email,code):
    # 发送html文本
    subject = 'python157'
    from_email ='mambaout0803@sina.com'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target = blank > https://www.djangoproject.com/ < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format('127.0.0.1',code)

    # 发送邮件所执行的方法以及所需的参数
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    # 发送的html文本的内容
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def user_register(request):
    '''
    处理用户注册请求的view
    :param request:
    :return:
    '''
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    # models.Mailbox(username=username,password=password,email=email)
    new_user = models.Mailbox.objects.create(user_nickname=username,user_password=password,user_email=email)
    print(new_user)
    code = make_confirm_string(new_user)
    print(code)    #测试打印验证码
    send_email(email,code)
    return HttpResponse('')

def user_confirm(request):
    '''
    用户处理用户发起邮箱验证的请求
    :param request:  用户发来的验证码
    :return:
    '''
    user_code = request.GET.get('code')
    confirm = models.confirm_string.objects.get(code=user_code)
    if confirm:
        #将用户状态改为可登录
        pass
    else:
        pass
