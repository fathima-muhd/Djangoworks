from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

#Function based
# def first(request):
#     if(request.method=='GET'):
#         return HttpResponse("First Page")

# def second(request):
#     if(request.method=='GET'):
#         return HttpResponse("Second Page")


#class based

class First(View):
    def get(self,request):
        return HttpResponse("First page")

class Second(View):
    def get(self,request):
        return HttpResponse("Second Page")



