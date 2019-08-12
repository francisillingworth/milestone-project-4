from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    author = models.ForeignKey(User, default=None)
    
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, default=None)
    issue = models.ForeignKey(Issue, default=None, null=True)
    
    
    def __str__(self):
        return self.comment
        
