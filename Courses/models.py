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

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    correct_answer = models.CharField(max_length=1024)
    options = models.JSONField()  # Pour stocker plusieurs choix

class Certificate(models.Model):
    student = models.ForeignKey('authentication.Etudiant', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(auto_now_add=True)
    certificate_image = models.ImageField(upload_to='certificates/')