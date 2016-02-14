import requests
import json
import os
from textblob import TextBlob
from django.http import HttpResponse

def getData(request):
    query = request.GET['q']
    print query

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
    


    jarticles = json.dumps(articles, ensure_ascii=True)
    return HttpResponse(jarticles)
    

from sklearn.cluster import KMeans
def kmcluster(articles, n_clusters=3):
    X = [art['sentiment'] for art in articles]
    km = KMeans(n_clusters)
    y = km.fit(X)
    for i in xrange(len(articles)):
        articles[i]['kmeans'] = y[i]
    return 

def bucket(articles, num_buckets = 10):
    for art in xrange(articles):
        art['bucket'] = (art['sentiment'] + 1) * 10

    
    
