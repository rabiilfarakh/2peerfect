# courses/models.py
from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    video = models.FileField(upload_to='videos/')  # Chemin où enregistrer les vidéos

    def __str__(self):
        return self.nom
