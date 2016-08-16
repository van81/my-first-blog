from __future__ import unicode_literals

from django.db import models

"""
    Django ������.
    ����� ������� � ���� ������� ��������� �������� � ����� ����� ����:
    1. �������.
    2. �����. � ������ �������� ����� ���� ��������� �������, ���� � 
        ��� �� ����� ����� ���� � ���������� ���������.
    3. ��������. � �������� ����� ���� ��������� ���������,
        �� ������ �������� ����� ������� ������ � ����� ��������.
        � ����� ������ ������ ���� ���� ����� �� ������.
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
  
