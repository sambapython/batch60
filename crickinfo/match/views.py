from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def users_fun(request):
	return HttpResponse("hello1234")
