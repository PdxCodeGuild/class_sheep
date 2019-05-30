from django.db import models

class UrlShortener(models.Model):
    code = models.CharField(max_length=20)
    url = models.CharField(max_length=200)


    def __str__(self):
        return self.url