from django.shortcuts import get_object_or_404, render
from schoolmanagement.models import School
from django.http import JsonResponse
# Create your views here.
__all__ = [
    "School_details",
    "School_list",
]

#crea due class-based view per rappresentare su template:
#a. i dettagli di una singola entry del model School; class School_details():  
#funzioni e non classi già definite x avere personalizzaz=inserimento utente dell’id scuola
def School_details(request, pk):
    scuola = get_object_or_404(School, pk=pk)
    return render(
        request,
        "schoolmanagement/school_detail.html",
        {"object": scuola}, #dizionario che mergiamo
    )

#b. la lista di tutte le entry del model School. class School_list(): 
def School_list(request):
    scuole = School.objects.all()
    return render(
        request,
        "schoolmanagement/school_list.html",
        {"object_list": scuole}, #mergiamo diz
    )

#def api_example(request):
    data = { 
        "nome" : "giulia", 
        "cognome" : "bellesia",
        }
    
    return JsonResponse(data) 


