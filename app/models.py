from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100, null=False)
    reviewer = models.CharField(max_length=100, null=False)
    stars = models.FloatField(null=False)
    comment = models.CharField(max_length=800, null=True)


class Result(models.Model):
    query = models.CharField(max_length=255, null=False)
    time = models.DateTimeField(auto_now_add=True)
    positive = models.FloatField(null=False)
    anger = models.FloatField(null=False)
    sadness = models.FloatField(null=False)
    disgust = models.FloatField(null=False)
    percent_positive = models.FloatField(null=False)
    percent_negative = models.FloatField(null=False)
