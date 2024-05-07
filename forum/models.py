from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)