from django.shortcuts import render
from .tasks import cadd
from django.http import HttpResponse
# Create your views here. 

def index(request):
	for i in range(3):
		cadd.delay()
	return HttpResponse("hello")