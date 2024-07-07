from django.db import models

class Meet(models.Model):
    title = models.CharField(max_length=255)
    meet_link = models.URLField(max_length=200)
    created_by = models.CharField(max_length=100)
    topic = models.CharField(max_length=255, blank=True, null=True)
    agenda = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
