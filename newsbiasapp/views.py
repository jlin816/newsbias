import requests
import json
import os
from django.http import HttpResponse

def getData(request):
    query = request.GET['q']

    query_parts = query.split()
    ALCHEMY_SECRET_KEY = os.environ['ALCHEMY_SECRET_KEY']
    url= "https://access.alchemyapi.com/calls/data/GetNews?apikey=" + ALCHEMY_SECRET_KEY +"&return=enriched.url.title,enriched.url.url,enriched.url.docSentiment&start=1454803200&end=1455490800&count=25&outputMode=json"

    for part in query_parts:
        url += "&q.enriched.url.enrichedTitle.keywords.keyword.text=" + part

    response = requests.get(url)
    data = json.loads(response.text)
    print response.text
    articles = []
    for jarticle in data['result']['docs']:
        link = jarticle['source']['enriched']['url']['url']
        title = jarticle['source']['enriched']['url']['title']
        sentiment = jarticle['source']['enriched']['url']['docSentiment']['score']
        articles.append({'link': link,
                         'title': title,
                         'sentiment': sentiment})
        
    jarticles = json.dumps(articles, ensure_ascii=False)
    print articles
    print
    print jarticles
    return HttpResponse(jarticles)
    
