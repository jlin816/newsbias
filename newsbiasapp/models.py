from django.db import models

class Article(models.Model):
    link = models.URLField()
    title = models.CharField(max_length = 100)
    sentiment = models.DecimalField(max_digits = 3, decimal_places = 2)
    img = models.ImageField()

