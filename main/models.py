from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=32)
    subject = models.ManyToManyField('Subject')
    role = models.CharField(max_length=8, choices=[('staff', 'Staff'), ('student', 'Student')])

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Time(models.Model):
    time = models.CharField(max_length=16)

    def __str__(self):
        return self.time


class Group(models.Model):
    time = models.ForeignKey('Time', on_delete=models.PROTECT)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
    teacher = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='teacher')
    students = models.ManyToManyField(Profile, related_name='students')

    def __str__(self):
        return f"Faxr-{self.pk}"
