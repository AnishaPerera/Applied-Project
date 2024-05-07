from django.db import models

# Create your models here.

class vulnerability_detail(models.Model):
    cve_id = models.CharField(max_length=100, primary_key=True)
    cvss_score = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    published_date = models.CharField(max_length=100)
    base_severity = models.CharField(max_length=100)
    mitigations = models.TextField()

    class Meta:
        managed = False
        db_table = 'vulnerabilities'
    
    def __str__(self):
        return self.cve_id

