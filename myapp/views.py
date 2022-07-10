from django.shortcuts import render, redirect, HttpResponse
from django.template import loader  
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django import forms
from .models import GeeksModel
from django.http import JsonResponse




################ All forms here ############
class MessageForm(forms.Form):
   name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name..','id':'pt1inp'}))
   email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your email..','id':'pt1inp'}))
   message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your message...','id':'txtarmsg'}))
class LoginForm(forms.Form):
   user = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your user..','id':'user'}))
   password = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your pass..','id':'pass'}))
   

@csrf_exempt
def view_function(request):
   if request.method =="POST":
      form= MessageForm(request.POST)
      if form.is_valid():
         print("yesssssssssssss")
         name = form.cleaned_data['name']
         email = form.cleaned_data['email']
         message = form.cleaned_data['message']
         print(email)
         return JsonResponse({"coins":"4","email":email})

def login_function(request):
   if request.method =="POST":
      form= LoginForm(request.POST)
      if form.is_valid():
         print("yesssssssssssss")
         user = form.cleaned_data['user']
         password = form.cleaned_data['password']
         return JsonResponse({"coins":"4","email":user})
# Create your views here.



@csrf_exempt
def index(request):
   form= MessageForm()
   
   return render(request, "index.html",{'form': form})

def login(request):
   form1= LoginForm()
   print(GeeksModel.objects.get(username = "palash").password)
   return render(request, "login.html",{'form_a': form1})
