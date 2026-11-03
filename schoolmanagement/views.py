from django.shortcuts import get_object_or_404, render
from schoolmanagement.models import School
# Create your views here.
__all__ = [
    "School_details",
    "School_list",
]

#crea due class-based view per rappresentare su template:
#a. i dettagli di una singola entry del model School; class School_details():  
#ha tenuto funzioni anche se ci sono classi già definite
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



