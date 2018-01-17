# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
	ID = models.IntegerField(primary_key=True)
	Article = models.CharField(max_length=100)
	Cost = models.DecimalField(max_digits=None, decimal_places=2)
	PriceVatExcl = models.DecimalField(max_digits=None, decimal_places=2)
	PriceVatIncl = models.DecimalField(max_digits=None, decimal_places=2)
	Creation = models.DateField(auto_now_add=True)
	LastChange = models.DateField(auto_now=True)
