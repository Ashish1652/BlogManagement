from django.db import models

# Create your models here.
class blog_model(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    summery = models.TextField()
    time = models.DateTimeField(auto_now=True)    #udate time
    time_update = models.DateTimeField(auto_now_add=True) #Add time