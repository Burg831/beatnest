from django.db import models

class Gig(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=120, blank=True)
    url = models.URLField(blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

