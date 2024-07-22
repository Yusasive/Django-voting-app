from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=10)
    nickname = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='candidate_photos/')

    def __str__(self):
        return f"{self.name} ({self.position})"
