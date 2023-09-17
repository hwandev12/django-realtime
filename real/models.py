from django.db import models

class Joke(models.Model):
    joke = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.joke
