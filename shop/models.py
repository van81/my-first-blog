from __future__ import unicode_literals

from django.db import models

"""
    Django ������.
    �㦭� ������ � ���� ������� ᫥���騥 ��魮�� � �裡 ����� ����:
    1. �������.
    2. �����. � ������ �������� ����� ���� ������⢮ ⮢�஢, ���� � 
        �� �� ⮢�� ����� ���� � ��᪮�쪨� ���������.
    3. �த����. � �������� ����� ���� ��᪮�쪮 �த��殢,
        �� ����� �த���� ����� ࠡ���� ⮫쪮 � ����� ��������.
        � ����� ������ ������ ���� ��� ����� �� ࠡ���.
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
  
