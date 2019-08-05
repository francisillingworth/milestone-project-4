from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    author = models.ForeignKey(User)
    
    
    def __str__(self):
        return self.name
        
