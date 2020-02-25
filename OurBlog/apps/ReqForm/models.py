from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=20,verbose_name='密码')
    email = models.EmailField(max_length=20,verbose_name='邮箱',null=True)
    phone = models.CharField(max_length=20,verbose_name='电话')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户:%s'%self.username
