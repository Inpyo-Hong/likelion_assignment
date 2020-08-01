from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=10)
    body = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField()
    