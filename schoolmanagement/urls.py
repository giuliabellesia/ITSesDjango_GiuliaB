"""
dentro app schoolmanagement con route puntatore a lista scuole ‘view.listascuole, nomelistascuole’ 
nel file della view di progetto aggiungiamo route delle scuole: school/ ci porta in school management url
abbiamo già page e about us, capiamo che admin→ admin site url, ora school→ school management url
include sempre da django ?
file di url del progetto include quello dell’app
se vai su 8000/school/ dovrebbe dire file not exist
"""

from django.urls import path
from schoolmanagement import views 

urlpatterns = [ 
    path("", views.School_list, name="School_list"), 
    #scritta così pk essendo inclusa significa che school/, registrata di là, mi da gia la lista di scuole senza aggiungere "" niente

    path("<int:pk>/", views.School_details, name="School_details"), 
    #scritta così perche int è id inserito da utente e primary key è la var corrispondente
    
    #path("api/v1/example/", views.api_example, name="api_example"),
]