from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

    
class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}의사 {self.patient_id}번 환자'