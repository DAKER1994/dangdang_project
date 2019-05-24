import os
from django.core.mail import send_mail, EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'project01.settings'
if __name__ == '__main__':

    #发送普通文本
    # send_mail(
    #     'Python157',
    #     '还能不能行',
    #     'mambaout0803@sina.com',
    #     ['shaonian1994@yeah.net'],
    #
    # )

    #发送html文本
    subject, from_email, to = 'python虐我千百遍', 'mambaout0803@sina.cn', 'shaonian1994@yeah.net'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target = blank > https://www.djangoproject.com/ < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '

    #发送邮件所执行的方法以及所需的参数
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #发送的html文本的内容
    msg.attach_alternative(html_content, "text/html")
    msg.send()









