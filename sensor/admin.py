# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from views import Room
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Room._meta.fields]
	list_editable=("temp","humi")
admin.site.register(Room,RoomAdmin)