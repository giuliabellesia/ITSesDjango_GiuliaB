from django.urls import path
from schoolapp.views import DOTWDetailView, DOTWListView, School_Courses

urlpatterns = [
    #path('classrooms/', views.Classrooms, name="Classrooms"),
    path('corsi/', School_Courses.as_view(), name="School_Courses"),
    path('calendario/', DOTWListView.as_view(), name="lista_giorni"),
    path('calendario/<int:pk>/', DOTWDetailView.as_view(), name="dettaglio_giorni"),
]
