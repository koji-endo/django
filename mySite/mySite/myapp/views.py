# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hi Dear World!")
def index_template(request):
	myapp_data={
	'app':'Django'
	}
	return render(request, 'index.html',myapp_data)
# Create your views here.
