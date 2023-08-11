from django.shortcuts import render
import requests
from bs4 import BeautifulSoup 
from rake_nltk import Rake 
import nltk 
import collections 
import difflib 
from .models import Tag, Advert 

#nltk.download()
#nltk.download('stopwords')
#nltk.download('punkt') 
# uncomment above commands for the first time use 
# go to command line and choose to download 'stopwords' corpus through nltk command-line prompt 

# Create your views here.
def index(request): 
    adsfound = False # Flag variable, keeps track of whether a search result is found or not  
    if request.method == 'POST': 
        url = request.POST.get('url')
        response = requests.get(url=url) 
        soup = BeautifulSoup(response.content, 'html.parser')   
        all_text = ''
        for para in soup.find_all('p'): 
            all_text += str(para.get_text())  
        rake_var = Rake() 
        rake_var.extract_keywords_from_text(all_text)  
        keywords_extracted = rake_var.get_ranked_phrases()  

        adtags = [] 
        tags = Tag.objects.all()  
        for tag in tags: 
            adtags.append(tag.tagname)
        
        seta = set(keywords_extracted) 
        setb = set(adtags)
        commonwords = []
        if(seta & setb): 
            commonwords = list(seta & setb) 

        relevantads =[]
        for advert in Advert.objects.all(): 
            for tag in advert.tags.all(): 
                if tag.tagname in commonwords: 
                    relevantads.append(advert) 
                    relevantads = set(relevantads)
                    relevantads = list(relevantads) 
        
        if relevantads: 
            adsfound = True

        context = {
            'relevantads': relevantads,
            'commonwords': commonwords,
            'adsfound': adsfound, 
            'blogUrl': url, 
        }

        return render(request, 'myapp/index.html', context) 

    return render(request, 'myapp/index.html') 
 
