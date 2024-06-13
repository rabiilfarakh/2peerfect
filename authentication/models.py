# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Permission as AuthPermission

class Group(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username = None
    first_name = None
    last_name = None
    role = models.CharField(max_length=20, choices=[('etudiant', 'Etudiant'), ('professeur', 'Professeur'), ('centre', 'Centre')], default='etudiant')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(AuthPermission, related_name='auth_user_permissions')

    class Meta:
        db_table = 'Users'

class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    experience = models.IntegerField()
    cv = models.BinaryField()
    remote = models.BooleanField(default=False)
    specialty = models.CharField(max_length=255)
    phone = models.IntegerField()

    class Meta:
        db_table = 'Professeurs'

class Centre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)
    capacity = models.IntegerField()
    phone = models.IntegerField()
    city = models.CharField(max_length=255)

    class Meta:
        db_table = 'Centers'

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    class Meta:
        db_table = 'Etudiants'
