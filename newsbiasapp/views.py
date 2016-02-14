from django.http import HttpResponse
import requests

def getData(request):
    #f = open("./api_key.txt", "r")
    #key = f.read().strip()
    # query = request.GET[''] #edit this
    ALCHEMY_SECRET_KEY = os.environ['ALCHEMY_SECRET_KEY']
    query = "bernie sanders"
    url= "https://access.alchemyapi.com/calls/data/GetNews?apikey=" + ALCHEMY_SECRET_KEY +"&return=enriched.url.title,enriched.url.url,enriched.url.docSentiment&start=1454803200&end=1455490800&count=25&outputMode=json&q.enriched.url.enrichedTitle.keywords.keyword.text=" + query
    response = requests.get(url)
    s = response.text
    
    return HttpResponse(s)
    