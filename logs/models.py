from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SearchLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    firmware_version = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user:{self.user} search - ({self.brand},{self.firmware_version}) ({self.timestamp})'
    
class AdvancedSearchLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, blank= True)
    firmware_version = models.CharField(max_length=100, blank=True)
    cve_id = models.CharField(max_length=100, blank=True)
    userquery = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user:{self.user} Search - ({self.brand},{self.firmware_version},{self.cve_id},{self.userquery}, API:{self.api_check}) ({self.timestamp})'