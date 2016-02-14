from django.http import HttpResponse
import requests
import os

def getData(request):
    #f = open("./api_key.txt", "r")
    #key = f.read().strip()
    query = request.GET['q']
    query_parts = query.split()
    ALCHEMY_SECRET_KEY = os.environ['ALCHEMY_SECRET_KEY']
    url= "https://access.alchemyapi.com/calls/data/GetNews?apikey=" + ALCHEMY_SECRET_KEY +"&return=enriched.url.title,enriched.url.url,enriched.url.docSentiment&start=1454803200&end=1455490800&count=25&outputMode=json"

    for part in query_parts:
        url += "&q.enriched.url.enrichedTitle.keywords.keyword.text=" + part

    response = requests.get(url)
    s = response.text
    
    return HttpResponse(s)
    