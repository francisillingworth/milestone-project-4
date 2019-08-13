from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    author = models.ForeignKey(User, default=None)
    
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, default=None, related_name='users')
    feature = models.ForeignKey('features.Feature', default=None, null=True, on_delete=models.CASCADE, related_name='comments')
    
    
    def __str__(self):
        return self.comment
        