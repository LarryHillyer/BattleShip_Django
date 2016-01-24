from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from rest_framework.decorators import  APIView

class index(APIView):
    def get(self,request):
        return render(request, "battleship/index.html")
        
    
    def post(self, request):
        userGuess = request.POST['user-guess']
        return HttpResponseRedirect(reverse('battleship:index'))
        

