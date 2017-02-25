from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100, null=False)
    reviewer = models.CharField(max_length=100, null=False)
    stars = models.FloatField(null=False)
    comment = models.CharField(max_length=800, null=True)
