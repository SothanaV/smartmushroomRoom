# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Room

from django.shortcuts import render

from django.http import HttpResponse
#from .models import Weather

from django.http import JsonResponse
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import sys
from django.contrib.auth.forms import PasswordChangeForm
from django.core import serializers

# Create your views here.
def getdata(request,nodeid,temp,humi,key):
	#node = request.POST['nodeid']
	if key=="1234567898765435678909890989098765432432342123432345678765434567":
		data_box = Room(
			nodeid = nodeid ,
			temp 	= float(temp), 
			humi 	= float(humi),
				)
		data_box.save()
		print (data_box)
		print (nodeid)
		print ("SAVE")
	else:
		print ("UnSAVE")
	
	return HttpResponse("Command",content_type='text/plain')


def showdata(request):

	#data = Room.objects.all().values('nodeid','temp','humi','time')
	data = Room.objects.all().order_by("-time").values('nodeid','temp','humi','time')[:1000:50] 
	return JsonResponse( list(data) , safe= False)
def graph(request):
	return render(request, 'first.html')
def amchart(request):
	return render(request, 'graph2.html')
