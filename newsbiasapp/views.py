import requests
import json
import os
from django.http import HttpResponse
#from newsbiasapp.models import Query
from itertools import izip
from collections import defaultdict
import operator
from django.db import models


def getData(request):
    myquery = request.GET['q']
    print myquery


    # Check if query results are already cached in the db
    if Query.objects.filter(query=myquery).exists():
        results = Query.objects.filter(query=myquery).json
        print results
        return HttpResponse(results)

    # Split into parts to allow AlchemyAPI to handle multiword queries
    query_parts = myquery.split()
    ALCHEMY_SECRET_KEY = os.environ['ALCHEMY_SECRET_KEY']
    url= "https://access.alchemyapi.com/calls/data/GetNews?apikey=" + ALCHEMY_SECRET_KEY +"&return=enriched.url.title,enriched.url.url,enriched.url.docSentiment,enriched.url.keywords&start=now-50&end=now&count=25&outputMode=json"

    for part in query_parts:
        query_url += "&q.enriched.url.enrichedTitle.keywords.keyword.text=" + part

    response = requests.get(query_url)
    data = json.loads(response.text)
    print response.text
    articles = []
    for jarticle in data['result']['docs']:
        link = jarticle['source']['enriched']['url']['url']
        title = jarticle['source']['enriched']['url']['title']
        sentiment = jarticle['source']['enriched']['url']['docSentiment']['score']
        keywords = [shit['text'] for shit in jarticle['source']['enriched']['url']['keywords']]
        kw_relevance = [shit['relevance'] for shit in jarticle['source']['enriched']['url']['keywords']]
        articles.append({'link': link,
                         'title': title,
                         'sentiment': sentiment,
                         'keywords': keywords,
                         'kw_relevance': kw_relevance})

    bucket(articles)
    kmcluster(articles)
    clus_kw = diff_keywords(articles, [art['kmeans'] for art in articles])
    jfinal = json.dumps({'articles': articles, 'cluster_kw': clus_kw}, ensure_ascii=True)

    return HttpResponse(jarticles)
    

from sklearn.cluster import KMeans
def kmcluster(articles, n_clusters=2):
    X = [[float(art['sentiment'])] for art in articles]
    km = KMeans(n_clusters) 
    print X
    km.fit(X)
    y = km.predict(X).tolist()
    for i in xrange(len(articles)):
        articles[i]['kmeans'] = y[i]

def bucket(articles, num_buckets = 10):
    for art in articles:
        art['bucket'] = (float(art['sentiment']) + 1) * 10 + 0.2

    
def diff_keywords(articles, cluster_ids):
    num_clusters = len(set(cluster_ids))
    cid_clus_w = [defaultdict(lambda: 0) for _ in xrange(num_clusters)]
    tot_w = defaultdict(lambda: 0)
    for art, c_id in izip(articles, cluster_ids):
        clus_w = cid_clus_w[c_id]
        for w,r in izip(art['keywords'], art['kw_relevance']):
            clus_w[w] += float(r)
            tot_w[w] += float(r)

    for w in tot_w:
        for clus_w in cid_clus_w:
            clus_w[w] /= tot_w[w]



    for i in xrange(num_clusters):
        curr_clus = cid_clus_w[i]
        for w in curr_clus:
            maxw = 0
            for j in xrange(num_clusters):
                other_clus = cid_clus_w[j]
                if i != j and (other_clus[w] > maxw):
                    maxw = other_clus[w]
            curr_clus[w] -= maxw


    clus_kw = [[] for _ in xrange(num_clusters)]

    for i in xrange(num_clusters):
        sorted_w = sorted(cid_clus_w[i].items(), key=operator.itemgetter(1), reverse=True)
        top10 = sorted_w[:10]
        for w,v in top10:
            clus_kw[i].append(w)


    return clus_kw

