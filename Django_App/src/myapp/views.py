from django.shortcuts import render
from .models import Character
# Create your views here.

def myapp_hi(request):
	return render(request,'helloworld.html',{})

def myapp_characters(request):
	character_list = Character.objects.all()
	return render(request,'character.html',{'characters':character_list})
