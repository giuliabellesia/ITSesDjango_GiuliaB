from django.db import models
from schoolmanagement.models import School
# Create your models here. elenco:
__all__ = [
    'DayOftheWeek',
    'Classroom',
    'Corso',
]

class DayOfTheWeek(models.Model):
    num = models.PositiveIntegerField(default=0);
    nome = models.CharField(max_length=20);

    def __str__(self):
        return self.nome

class Classroom(models.Model):
    nome = models.CharField(max_length=20);
    capacita = models.PositiveIntegerField(default=0);

    def __str__(self):
        return f"{self.nome}, capacita: {self.capacita}"

class Corso(models.Model):
    subject = models.CharField(max_length=30);
    orario_inizio = models.PositiveIntegerField(default=0);

    giorno = models.ForeignKey(#(foreign key a DayOfTheWeek):
        DayOfTheWeek,
        on_delete=models.CASCADE,
        related_name="corsi"
    ); 
    classroom = models.ForeignKey(#(foreign key a Classroom)
        Classroom,
        on_delete=models.CASCADE,
        related_name="corsi"
    ); 
    scuola = models.ForeignKey(#(foreign key a School)
        School,
        on_delete=models.CASCADE,
        related_name="corsi"
    ); 

    def __str__(self):
        return f"{self.subject}: {self.giorno} alle {self.orario_inizio}"