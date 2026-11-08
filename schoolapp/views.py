#from django.shortcuts import render, get_object_or_404
from django.views import generic
from schoolapp.models import DayOfTheWeek, Corso#, Classroom

# Create your views here.
__all__ = [
    "School_Courses", 
    #"CLassrooms",
    "DOTWListView",
    "DOTWDetailView",
]

#funzioni che prendono dati da models(dove ho tabelle), li renderizzano in tabelle carine e passano a template
#metti oggetti di contesto

class School_Courses(generic.ListView):#se voglio tabella corsi
    model = Corso

# def Classrooms(pk): #se voglio lista aule
#    aula = get_object_or_404(Classroom, pk=pk)
#    return render()

class DOTWListView(generic.ListView): 
    model = DayOfTheWeek 
    #elenco di tutti i giorni, il quale può rimandare a pag giorno specifica

class DOTWDetailView(generic.DetailView):
    model = DayOfTheWeek
    #dettagli singolo giorno=corsi collegati (giorno è foreignkey x corsi)