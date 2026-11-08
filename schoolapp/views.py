#from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from schoolapp.models import DayOfTheWeek, Corso, Classroom

# Create your views here.
__all__ = [
    "School_CoursesLV", 
    "School_CoursesDV", 
    "CLassroomsLV",
    "CLassroomsDV",
    "DOTWCreateView",
    "DOTWUpdateView",
    "DOTWListView",
    "DOTWDetailView",
]

#funzioni che prendono dati da models(dove ho tabelle), li renderizzano in tabelle carine e passano a template
#metti oggetti di contesto

class School_CoursesLV(generic.ListView):#se voglio tabella corsi
    model = Corso

class School_CoursesDV(generic.DetailView):#se voglio tabella corsi
    model = Corso

class ClassroomsLV(generic.ListView): #se voglio lista aule
    model = Classroom

class ClassroomsDV(generic.DetailView): 
    model = Classroom

class DOTWCreateView(generic.CreateView):
    model = DayOfTheWeek
    campi = ["nome", "numero"]
    success_url = reverse_lazy("lista_giorni")

class DOTWUpdateView(generic.UpdateView):
    model = DayOfTheWeek
    campi = ["nome", "numero"]

    def get_success_url(self):
        return reverse_lazy("dettaglio_giorno", kwargs={"pk": self.object.pk})

class DOTWListView(generic.ListView): 
    model = DayOfTheWeek 
    #elenco di tutti i giorni, il quale può rimandare a pag giorno specifica

class DOTWDetailView(generic.DetailView):
    model = DayOfTheWeek
    #dettagli singolo giorno=corsi collegati (giorno è foreignkey x corsi)