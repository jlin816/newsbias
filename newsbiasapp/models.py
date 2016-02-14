from django.db import models

class Query(models.Model):
    query = models.CharField(max_length = 50)
    json = models.TextField()
    #link = models.URLField()
    #title = models.CharField(max_length = 100)
    #sentiment = models.DecimalField(max_digits = 3, decimal_places = 2)

