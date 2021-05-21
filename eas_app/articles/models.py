from django.db import models
from datetime import datetime, date

class Article(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=False, auto_now=False)
    description = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.title

