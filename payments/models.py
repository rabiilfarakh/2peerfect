#payments/models.py
from django.db import models
from authentication.models import Etudiant
from Courses.models import Course

class Payment(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])

    class Meta:
        db_table = 'Payments'

    def __str__(self):
        return f"Payment {self.id} - {self.etudiant.user.name} - {self.course.nom}"
