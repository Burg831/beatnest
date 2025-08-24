from django.db import models

class Gig(models.Model):
    title     = models.CharField(max_length=200, db_index=True)
    company   = models.CharField(max_length=200, db_index=True)
    location  = models.CharField(max_length=200, db_index=True)
    url       = models.URLField(blank=True)
    posted_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-posted_at",)
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["company"]),
            models.Index(fields=["location"]),
        ]

