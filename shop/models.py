from __future__ import unicode_literals

from django.db import models

"""
    Django модели.
    Нужно описать в виде моделей следующие сущности и связи между ними:
    1. Магазин.
    2. Товар. В каждом магазине может быть множество товаров, один и 
        тот же товар может быть в нескольких магазинах.
    3. Продавец. В магазине может быть несколько продавцов,
        но каждый продавец может рабоать только в одном магазине.
        В полях модели должна быть дата найма на работу.
"""

class Shop(models.Model):
  name = models.TextField()


class Good(models.Model):
  name = models.TextField()
  shops = ManyToManyField(Shop)
  

class Seller(models.Model):
  name = models.TextField()
  shop = models.ForeignKey(Shop)
  startjob = models.DateTimeField(default=timezone.now)
  
