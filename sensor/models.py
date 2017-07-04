# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Room(models.Model):
    time    = models.DateTimeField(auto_now_add=True)
    nodeid  = models.CharField(max_length=3, blank=False)
    temp    = models.FloatField(default=0.0)
    humi    = models.FloatField(default=0.0)
    class Meta:
        ordering = ['nodeid']