from django.urls import path
from schoolapp.views import DOTWDetailView, DOTWListView, School_CoursesLV, School_CoursesDV, ClassroomsLV, ClassroomsDV, DOTWCreateView, DOTWUpdateView

urlpatterns = [
    path('classrooms/', ClassroomsLV.as_view(), name="lista_aule"),
    path('classrooms/<int:pk>/', ClassroomsDV.as_view(), name="dettaglio_aula"),
    path('corsi/', School_CoursesLV.as_view(), name="lista_corsi"),
    path('corsi/<int:pk>/', School_CoursesDV.as_view(), name="dettaglio_corso"),
    path('calendario/', DOTWListView.as_view(), name="lista_giorni"),
    path('calendario/aggiungi/', DOTWCreateView.as_view(), name="crea_giorno"),
    path('calendario/<int:pk>/', DOTWDetailView.as_view(), name="dettaglio_giorno"),
    path('calendario/<int:pk>/modifica', DOTWUpdateView.as_view(), name="modifica_giorno"),
]
