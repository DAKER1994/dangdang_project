# from django.contrib.auth.handlers.modwsgi import check_password
import hashlib
import random
import re
import string
from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from xmapp import models
from xmapp.cart import Cart
from xmapp.models import TBook,TClassify,TAddress,TOrder,TOrderitem,TUser
# Create your views here.
from django.contrib.auth.hashers import make_password,check_password
from captchaapp.captcha.image import ImageCaptcha

def getcaptcha(request):
    image = ImageCaptcha()
    rand_code = random.sample(string.ascii_letters + string.digits,1)
    rand_code = "".join(rand_code)
    request.session['code'] = rand_code
    data = image.generate(rand_code)
    return HttpResponse(data,'image/png')

def index(request):
    a = TClassify.objects.filter(category_pid=0)
    b = TClassify.objects.filter(category_pid__gte=1)
    c = TBook.objects.all().order_by('shelves_date')[0:11]
    d = TBook.objects.all()[0:11]
    e = TBook.objects.all()[0:3]
    f = TBook.objects.all()[5:8]
    # print(make_password('123456'))
    #测试
    # print(check_password('123456','pbkdf2_sha256$100000$avflzVXjL8nr$QERoI/gCaFrmzniiL3iLUiZ9aYjHm9NsDfEGDeFJYfM='))
    # print(a,b,c,d)
    return render(request,'xmapp/index.html',{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f})

def details(request):
    id= request.GET.get('id')
    g = TBook.objects.filter(pk=id)[0]
    print(g)
    h = g.classif
    print(h)
    s = h.category_pid
    w = TClassify.objects.filter(pk=s)[0]

    print(w)
    return render(request,'xmapp/Book details.html',{'g':g,'h':h,'w':w,'id':id})

def booklist(request):
    r = TClassify.objects.filter(category_pid=0)
    n = TClassify.objects.filter(category_pid__gte=1)

    id= request.GET.get('id')
    # g = TBook.objects.filter(pk=id)[0]
    # h = g.classif
    # s = h.category_pid
    # w = TClassify.objects.filter(pk=s)[0]
    # g = TBook.objects.filter(pk=id)[0]

    id1 = request.GET.get("id1")
    id2 = request.GET.get("id2")
    number = request.GET.get('number')
    l = []
    if not number:
        number= 1
    if id2 =='0':
        class2 = TClassify.objects.filter(category_pid=id1)
        for i in class2:
            l.append(i.id)
            for j in l:
                books = TBook.objects.filter(classif=j)
    else:
        books = TBook.objects.filter(classif=id1)
    pagtor = Paginator(books,per_page=3)
    page = pagtor.page(number)
        # page_num = number
        # a = TBook.objects.all()[0:11]
        # books = TBook.objects.all()
        # pagtor = Paginator(books,per_page=5)
        # page = pagtor.page(page_num)
    return render(request,'xmapp/booklist.html',{'page':page,'number':number,'id1':id1,'id2':id2,'r':r,'n':n})

def regist(request):

    return render(request,'xmapp/register.html')

def regist_ok(requst):
    return render(requst,'xmapp/register ok.html')


def hash_code(nickname, now):
    h = hashlib.md5()
    nickname += now
    h.update(nickname.encode())
    return h.hexdigest()


def make_Confirm_string(new_user):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mailcode = hash_code(new_user.user_nickname, now)
    models.Confirm_string.objects.create(code=mailcode, user=new_user)
    return mailcode


def send_email(email,mailcode):
    # 发送html文本
    subject = 'python157'
    from_email ='mambaout0803@sina.cn'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target = blank > https://www.djangoproject.com/ < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format('127.0.0.1',mailcode)

    # 发送邮件所执行的方法以及所需的参数
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    # 发送的html文本的内容
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def user_confirm(request):
    '''
    用户处理用户发起邮箱验证的请求
    :param request:  用户发来的邮箱验证码
    :return:
    '''
    user_code = request.GET.get("txt_pop_sms_vcode")
    confirm = models.Confirm_string.objects.get(code=user_code)
    if confirm:
        #将用户状态改为可登录
        pass
    else:
        pass


def regist_logic(request):
    try:
        with transaction.atomic():
            email = request.POST.get('txt_username')   #获取邮箱
            password = request.POST.get('txt_password')
            password2 = request.POST.get('txt_repassword')
            nickname = request.POST.get('nickname')      #获取昵称
            captcha = request.POST.get("txt_vcode").upper()
            code = request.session.get("code").upper()
            request.session['name'] = email
            # return redirect('xmapp:index')
            dataname = TUser.objects.filter(user_email=email)
            pwd_j = make_password(password)
            flag = request.POST.get('flag')
            print(flag)
            if flag == 'index':
                pass

                # request.session['login'] = 'ok'
            if not dataname and password == password2 and code == captcha:
                new_user = models.TUser.objects.create(user_nickname=nickname, user_password=pwd_j, user_email=email)
                print(new_user)
                mailcode = make_Confirm_string(new_user)
                print(mailcode)  # 测试打印验证码
                send_email(email, mailcode)
                # u = TUser.objects.create(user_email=email,user_password=pwd_j,has_confirm=1,user_nickname=nickname)
                # u.save()  #保存
                # print(u)
                if new_user:
                    request.session['name']=email
                    request.session['login'] = 'ok'
                    return redirect('xmapp:index')
            return redirect('xmapp:regist')


            # if captcha.upper()==code.upper()and result2:
            #     return redirect('loginapp:login')
    except Exception as e:
        print(e)    #检测异常
        return render(request,'xmapp/register.html')


def login(request):
    name = request.COOKIES.get('txtUsername')
    password = request.COOKIES.get('txtPassword')
    result = TUser.objects.filter(user_email=name,user_password=password)
    if result:
        request.session['login'] = 'ok'
        return redirect('xmapp:index')
    return render(request,'xmapp/login.html')


def loginlogic(request):
    username = request.POST.get('txtUsername')
    password = request.POST.get('txtPassword')
    # result = TUser.objects.filter(user_email=name,user_password=password)
    codec = request.POST.get('txtVerifyCode')
    code = request.session.get('code')
    flag = request.POST.get('flag')
    rem = request.POST.get('autologin')
    # print(rem,123456)
    # print(code,flag)
    if  code != codec:
        return render(request,'xmapp/login.html')
    userlist = TUser.objects.filter(user_email=username)
    for user in userlist:
        checkpassword = user.user_password
    checkpwdjm = check_password(password,checkpassword)
    res = redirect('xmapp:index')
    if checkpwdjm:
        if flag == 'index':
            if len(userlist) > 0:
                request.session['name'] = username
                request.session['login'] = 'ok'
                if rem:
                    res.set_cookie('txtUsername', username, max_age=7 * 24 * 3600)
                    res.set_cookie('txtPassword', password, max_age=7 * 24 * 3600)
                flag = None
                return res
                # return redirect('xmapp:index')

    return render(request,'xmapp/login.html')




    # print(result,codec,code)    #测试

    # if result:
    #     res = redirect('xmapp:index')
    #     request.session['login']='ok'



'''
    if  result and codec.upper ==code.upper:
        res = redirect('xmapp:index')
        request.session['login']='ok'
        res.set_cookie('user_email',name,max_age=7*24*3600)
        res.set_cookie('user_password',password,max_age=7*24*3600)
        # print(1561615615)     # 若判断正确将执行这步
        return res
    return render(request,'xmapp/login.html')
'''



def checklogincode(request):
    number = request.GET.get('txtVerifyCode')
    code = request.session.get('code')
    print(number,code)
    if number.upper()==code.upper():
        return HttpResponse('1')
    else:
        return HttpResponse('2')


def logout(request):
    del request.session['name']
    return HttpResponse('ok')



def indent(request):
    flag = request.GET.get('flag')
    request.session['flag'] = flag
    username = request.session.get('name')
    cart = request.session.get('cart')
    if username:
        print("这个是用户名",username)
        t = TUser.objects.get(user_email=username)
        addr = TAddress.objects.filter(user_id=t.id)
        return render(request,'xmapp/indent.html',{'addr':addr,'cart':cart})
    else:
        return redirect('xmapp:loginlogic')


    # try:
    #     flag = request.GET.get('flag')
    # except Exception:
    #     flag = ''
    # data = request.POST.get('book_id_list')
    # if data:
    #     request.session['list_id'] = data.split(',')
    # if not username and not flag:
    #     request.session['flag'] = 1
    #     return render(request,'xmapp/login.html')
    # #在订单提交的同时把购物车清空
    # del request.session['cart']
    # del request.session['price']
    # del request.session['flag']
    # #定义一个列表，用于存储重新组织的数据
    # list1 =[]
    # list_book_id = request.session.get('list_id')
    # #接收传递过来的书籍id以及数量
    # n = int(len(list_book_id))
    # # 把每本书的id和数量组成一个元组进行操作
    # for i in range(0,n,2):
    #     list1.append((list_book_id[i],list_book_id[i+1]))
    #     #根据id查询出每个书籍的信息，用于存放在订单表中，并传递到页面中
    #     #定义一个列表存放要传递到页面中的信息
    #     total_price = 0
    #     listbooks = []
    #     user = TUser.objects.get(user_email=username)
    #     #现根据用户id查看是否有地址信息
    #     addr = TAddress.objects.filter(detail_address=user.id)
    #     with transaction.atomic():
    #         user.torder_set.create(status=0)
    #     order_n = TOrder.objects.all()[len(TOrder.objects.all())-1]
    #
    #     for i in list1:
    #         #每本书籍的信息
    #         book = TBook.objects.get(id=i[0])
    #         discount = (book.dd_pricing/book.pricing)*10
    #         oneprice = int(i[1])*book.dd_pricing
    #         listbooks.append((book.bookname,book.dd_pricing,book.pricing,i[1],oneprice,book.press,discount,book.id))



def indent_ok(request):
    return render(request,'xmapp/indent ok.html')


def indent_ajax1(request):
    a = request.GET.get('a')
    b = TAddress.objects.filter(detail_address=a)
    def mydefault(n):
        if isinstance(n,TAddress):
            return {'id':n.id,'name':n.receive_name,'address':n.detail_address,'zipcode':n.zipcode,'telphone':n.telphone,'cellphone':n.cellphone,'userid':n.user_id}
    return JsonResponse(list(b),safe=False,json_dumps_params={"default":mydefault})








def checkemail(request):
    email = request.POST.get('email')
    #验证邮箱格式
    result = TUser.objects.filter(user_email=email)
    if result:
        return HttpResponse('no')
    else:
        return HttpResponse('ok')


    #     try:
    #         result = TUser.objects.filter(user_email=name)
    #     except Exception:
    #         result = None
    #     if result:
    #         return HttpResponse('2')
    #     else:
    #         return HttpResponse('3')
    # return HttpResponse('1')




def checkpwd(request):
    userpwd1 = request.GET.get('txt_password')
    userpwd2 = request.GET.get('txt_repassword')
    print(userpwd1,userpwd2)
    if userpwd1 ==userpwd2 and userpwd2 !='' and userpwd1 !='':
        return HttpResponse('密码正确')
    elif userpwd1=='' or userpwd2 == '':
        return HttpResponse("密码不能为空")
    else:
        return HttpResponse('两次密码输入不一致')


def checknum(request):
    number = request.GET.get('txt_vcode')
    code = request.session.get('code')
    # print(number,code)
    if number.upper()==code.upper():
        return HttpResponse('1')
    else:
        return HttpResponse('2')




# 购物车
def add_book(request):
    # 接收参数
    id = request.GET.get("id")
    num = request.GET.get('num')
    print(id,type(id),num,12345)
    cart = request.session.get('cart')
    p = TBook.objects.filter(pk=int(id))[0]

    if cart is None:
        cart =Cart()
        cart.add_book_toCart(p.id,int(num))
        request.session['cart'] = cart
    else:
        cart.add_book_toCart(p.id,int(num))
        request.session['cart'] = cart
    return HttpResponse('ok')

def car(request):
    info = request.session.get('cart')
    # print(info)
    if not info:
        info = Cart()
    goods_info = info.cartitem
    total_price = info.total_price
    save_price = info.save_price
    print(total_price)
    print(goods_info)


    return render(request,'xmapp/car.html',{'total_price':total_price,'goods_info':goods_info,'info':info,'save_price':save_price})

    # site = TAddress.objects.all()[0:11]
    # print(site)
 #    '''
 #    if not request.session.get('cart'):
 #        request.session['cart'] = ''
 #        if request.session.get('to_cart'):
 #            request.session['cart'] = request.session.get('to_cart')
 #            del request.session['to_cart']
 #    if not request.session.get('price'):
 #        request.session['price'] = ''
 #        request.session['price'] = request.session.get('to_price')
 #        del request.session['to_price']
 #    cart = request.session.get('cart')
 #    data = request.session.get('price')
 #    print(data)
 #    save_price = 0
 #    total_price = 0
 #    if not cart or not data:
 #        return render(request,'xmapp/car.html',{'cart':'','total_save':'','total_real':''})
 #    print(data)
 #    for w in data:
 #        save_price += data[w][1]
 #        total_price += data[w][0]
 #
 #    return render(request,'xmapp/car.html',{'cart':cart,'save_price':save_price,'total_price':total_price})
 # '''


def del_book_info(request):
    bookid = request.GET.get('bookid')
    print(bookid)
    info = request.session.get('cart')
    info.delete_book(bookid)
    request.session['cart'] = info
    return redirect('xmapp:car')



