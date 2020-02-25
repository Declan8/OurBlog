from django.db import models

# Create your models here.

class Example(models.Model):
    name = models.CharField(max_length=32,verbose_name='案例的名称')
    type = models.CharField(max_length=32,verbose_name='案例的类型')

    def __str__(self):
        return self.name
