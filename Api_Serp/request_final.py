import json
import time
import requests
from translate import Translator


class playload():
  def __init__(self,keyword,country ,language ,autocorrect=True) :
    self.payload = json.dumps({
        "q": keyword,
        "gl": country,
        "hl": language,
        "autocorrect": autocorrect}) 
  def get(self):
    return self.payload
  def set(self,keyword,country ,language ,autocorrect=True):
    self.payload = json.dumps({
        "q": keyword,
        "gl": country,
        "hl": language,
        "autocorrect": autocorrect}) 
def request_img(payload ,headers):
    url = "https://google.serper.dev/images"
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)
    images = res["images"]
    m = images[1]
    imageUrl = m["thumbnailUrl"]
    imageUrl = imageUrl
   
    return  imageUrl
    
def request_organic(payload ,headers):
    url = "https://google.serper.dev/search"
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)
    words = res["relatedSearches"]
    Section_keywords = []
    for word in words :
      Section_keywords.append(word["query"])
    return  Section_keywords


def return_section2(h1_list):
  section_2 = """"""
  for i in h1_list :
    lenth = len(section_2)+len(i)
    if lenth <= 125 : 
      section_2 +=  i +'\n'
  return section_2


 
def article(keyword,section_number,api_token,language,country):
  headers = {
        'X-API-KEY': api_token,
        'Content-Type': 'application/json'}   
  titre1 = keyword
  country = country.lower()
  pl = playload(titre1,country,language ,autocorrect=True)
  
  json_back = {}
  first_section = {}
  first_section['main_title'] = {titre1}
  img1 = request_img(pl.get(),headers)
  first_section["img"]=img1

  list_of_article_keyword = request_organic(pl.get(),headers)
  sec2 = return_section2(list_of_article_keyword)
  first_section["section_2"] = sec2
  json_back["section_main"] = first_section

  full_h2 = []
  sectionh2 = []
  imgs = []
  
  for t in range(section_number) :
    section_back = {}
    titre = list_of_article_keyword[t] 

    pl = playload(titre,"eg","ar" ,autocorrect=True)
    img = request_img(pl.get(),headers)
    list_of_article_keyword_2 = request_organic(pl.get(),headers)
    sec2 = return_section2(list_of_article_keyword_2)
    section_back['titre']= titre
    section_back['section_2']= sec2
    titre = "<h2>"+ titre +"<h2>"
    full_h2.append(titre)
    
    imgs.append(img)
    sectionh2.append(section_back)
    
    time.sleep(5)
  json_back["sections"] = sectionh2
  video_link = video (titre1,api_token,language,country )
  #------------------------------------------------
  sourc_list = source (titre1,api_token,language,country )
  #------------------------------------------------
  json_back["source"] = sourc_list
  json_back["video_link"] = video_link
  return json_back

def request_video(payload ,headers):
    url = "https://google.serper.dev/search"
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)
    
    organic = res["organic"]
    link = organic[0]
    video = link["link"]
    
    
    return  video
def video (keyword,api_token,language,country ):
  keyword = "youtube" + keyword
  country = country.lower()
  pl = playload(keyword,country,language ,autocorrect=True)
  headers = {
        'X-API-KEY': api_token,
        'Content-Type': 'application/json'} 
  video = request_video(pl.payload,headers)
  return video

def trans (keyword,language):

  if (language == "en") : 
    translator= Translator(to_lang="fr", from_lang='en')
    language = "fr"
    
  else:  
    translator= Translator(to_lang="en", from_lang=language)
    language = "en"
    
  keyword = translator.translate(keyword)
  return keyword , language



def request_source(payload,headers):
    url = "https://google.serper.dev/search"
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)
    source = []
    organic = res["organic"]
    for n in organic : 
      source.append(n["link"])
    return source



def source (keyword,api_token,language,country ):
  keyword, language = trans(keyword,language)
  country = country.lower()
  pl = playload(keyword,country,language ,autocorrect=True)
  headers = {
        'X-API-KEY': api_token,
        'Content-Type': 'application/json'} 
  source = request_source(pl.payload,headers)
  return source 





