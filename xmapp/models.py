# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    receive_name = models.CharField(max_length=20)
    detail_address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=20)
    telphone = models.CharField(max_length=20, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    bookname = models.CharField(max_length=40, blank=True, null=True)
    author = models.CharField(max_length=40, blank=True, null=True)
    press = models.CharField(max_length=40, blank=True, null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    edition = models.CharField(max_length=40, blank=True, null=True)
    printing_time = models.DateTimeField(blank=True, null=True)
    impression = models.CharField(max_length=40, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pricing = models.FloatField(blank=True, null=True)
    words_number = models.CharField(max_length=40, blank=True, null=True)
    page_number = models.CharField(max_length=40, blank=True, null=True)
    format = models.CharField(max_length=40, blank=True, null=True)
    paper = models.CharField(max_length=40, blank=True, null=True)
    packaging = models.CharField(max_length=40, blank=True, null=True)
    dd_pricing = models.FloatField(blank=True, null=True)
    editor = models.CharField(max_length=40, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    author_content = models.CharField(max_length=200, blank=True, null=True)
    directory = models.CharField(max_length=40, blank=True, null=True)
    comment = models.CharField(max_length=40, blank=True, null=True)
    illustration = models.CharField(max_length=150, blank=True, null=True)
    classif = models.ForeignKey('TClassify', models.DO_NOTHING, db_column='classif', blank=True, null=True)
    customer_score = models.CharField(max_length=20, blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    market_status = models.CharField(max_length=20, blank=True, null=True)
    shelves_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TClassify(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=20, blank=True, null=True)
    book_counts = models.CharField(max_length=20, blank=True, null=True)
    category_pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_classify'


class TOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    order_addrid = models.ForeignKey(TAddress, models.DO_NOTHING, db_column='order_addrid', blank=True, null=True)
    order_uid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='order_uid', blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderitem(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_bookid = models.ForeignKey(TBook, models.DO_NOTHING, db_column='shop_bookid', blank=True, null=True)
    shop_num = models.IntegerField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_orderitem'


class TUser(models.Model):
    user_email = models.EmailField(verbose_name='邮箱')
    user_nickname = models.CharField(max_length=128, blank=True, null=True)
    user_password = models.CharField(max_length=50, blank=True, null=True)
    c_time = models.DateTimeField(auto_now_add=True)
    # user_status = models.CharField(max_length=20, blank=True, null=True)
    has_confirm = models.BooleanField(default=False, verbose_name='是否确认')
    class Meta:
        # managed = False
        db_table = 't_user'


class Confirm_string(models.Model):
    code = models.CharField(max_length=256,verbose_name='用户注册码')
    user = models.ForeignKey('TUser',on_delete=models.CASCADE,verbose_name='关联的用户')
    code_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 't_confirm_string'






