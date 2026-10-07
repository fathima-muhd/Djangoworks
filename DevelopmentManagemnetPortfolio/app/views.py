from django.shortcuts import render

from django.http import JsonResponse
from django.views import View

class About(View):
    def get(self,request):
        data={"id":101,"full":"Fathima Muhammed","Title":"Python developer","DOB":"24-12-2003","email":"fathi232gmail.com","contact":7689786778,"Location":"Kochi","github url":"github.com/fathima-muhd","linkedin":"linkedin.com/in/fathima-muhammed818499292"}
        return JsonResponse(data)

class Education(View):
    def get(self,request):
        data={ "id":102,"institution":"Luminar","course":"Python","university":"KTU", "location":"Tvm", " startyear":2022, "Endyear":2026, " Grade":"A","description":"Computer science"}
        return JsonResponse(data)


class Project(View):
    def get(self,request):
        data=[{"id":101,"projectname":"Facial recognition","description":"detecting criminals", "technologies":"GAN", "duration":"6 months" ,"liveurl":"https://github.com/devikavr7447/crime-web"},
              {"id":102,"projectname":"Facial attendance","description":"mark attendance using facial features", "technologies":"CNN", "duration":"6 months" ,"liveurl":"https://github.com/fathima7447/crime-web"},
              {"id":103,"projectname":"Dog collar","description":"monitoring dogs", "technologies":"resnet", "duration":"7 months" ,"liveurl":"https://github.com/hasna7447/crime-web"}
              ]
        return JsonResponse(data,safe=False)