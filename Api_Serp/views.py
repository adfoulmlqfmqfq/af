from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .app import feel_ing
from .request_final import article
api_token = 'ec3e2412d3d6e96e32039c78f735c2699a9072b0'
our_token = '71d169a1'
@api_view(['GET', 'POST'])
def serp_api(request):
  data = {}
  if request.method == 'GET':
        final = {}
        sucess = ""
        key = ''
        try:
          key = request.query_params["key"]
        except:
            final['error'] = 'no key'
            return Response(final) 
        try:
            pass
        except:
            final['error'] = 'AI Algorithme'
            return Response(final) 
        
        english , arabic = feel_ing(key)
        # Get prediction
        
        final['feeling english'] = english 
        final['feeling arabic'] = arabic 
        return Response(final)
  #else:
    #data["detail"]="Bad Request"
    #return Response(data,status= status.HTTP_400_BAD_REQUEST)

#{"keyword":" بشرة","section_number" :2 ,"token" :"71d169a1" ,"language":"ar","country" :"eg" }