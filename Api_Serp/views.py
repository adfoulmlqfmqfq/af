from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .request_final import article
api_token = 'ec3e2412d3d6e96e32039c78f735c2699a9072b0'
our_token = '71d169a1'
@api_view(['GET', 'POST'])
def serp_api(request):
  data = {}
  if request.method == 'POST':
    try : 
      data = JSONParser().parse(request)
      token = data["token"]
      if token == our_token:
        keyword = data['keyword']
        section_number = data['section_number']
        if type(section_number) == type('str'):
          print('str')
          section_number = int(section_number)
        language= data['language']
        country = data['country']
        
      else : 
        data["detail"]="Bad Token "
        return Response(data ,status=status.HTTP_401_UNAUTHORIZED)
       
    except Exception as e: 
       data["detail"]="Bad Request POST"
       return Response(data,status= status.HTTP_400_BAD_REQUEST) 
    try:
          article_res = article(keyword,section_number,api_token,language,country)
    except:
          data["detail"]="Bad Serp request "
          return Response(data,status= status.HTTP_400_BAD_REQUEST) 
    return Response(article_res)
  else:
    data["detail"]="Bad Request"
    return Response(data,status= status.HTTP_400_BAD_REQUEST)

#{"keyword":" بشرة","section_number" :2 ,"token" :"71d169a1" ,"language":"ar","country" :"eg" }