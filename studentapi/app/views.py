from django.shortcuts import render

from django.http import JsonResponse
from django.views import View

class Studentdetails(View):
    def get(self,request):
        data={"name":"Fathima","age":22,"course":"python"}
        return JsonResponse(data)

class StudentList(View):
    def get(self,request):
        data=[{"name":"Fathima","age":22,"course":"python"},
        {"name":"Farhah","age":24,"course":"Data analytics"},
        {"name":"Devika","age":23,"course":"Data Science"}]
        return JsonResponse(data,safe=False)