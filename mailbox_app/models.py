# from django.db import models
#
# # Create your models here.
#
# class Mailbox(models.Model):
#     user_nickname = models.CharField(max_length=128,verbose_name='用户名')
#     user_password = models.CharField(max_length=40,verbose_name='密码')
#     user_email = models.EmailField(verbose_name='邮箱')
#     c_time = models.DateTimeField(auto_now_add=True)
#     has_confirm = models.BooleanField(default=False,verbose_name='是否确认')
#     class Meta:
#         db_table='t_mailbox'
#
# class confirm_string(models.Model):
#     code = models.CharField(max_length=256,verbose_name='用户注册码')
#     user = models.ForeignKey('Mailbox',on_delete=models.CASCADE,verbose_name='关联的用户')
#     code_time = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 't_confirm_string'