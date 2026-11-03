from django.db import models
# Create your models here. elenco:
__all__ = [
    'DayOftheWeek',
    'Classroom',
    'Course',
]

class DayOfTheWeek(models.Model):
    number = models.CharField(max_length=5);
    name = models.CharField(max_length=20);

class Classroom(models.Model):
    name = models.CharField(max_length=20);
    capacity = models.CharField(max_length=5);

class Course(models.Model):
    subject = models.CharField(max_length=30);
    day_of_the_week = models.CharField(max_length=5); #(foreign key a DayOfTheWeek);
    starting_hour = models.CharField(max_length=7);
    classroom = models.CharField(max_length=20); #(foreign key a Classroom)
    school = models.CharField(max_length=30) #(foreign key a School)