from django.db import models

__all__ = [
    "School",
]

# Create your models here.
class School(models.Model): 
    name = models.CharField(max_length=100);
    street = models.CharField(max_length=200);
    city = models.CharField(max_length=100);
    province = models.CharField(max_length=100);
    zip_cap = models.CharField(max_length=20);
    country = models.CharField(max_length=100);
    website = models.URLField(max_length=200, blank=True);
    phone = models.CharField(max_length=20, blank=True);
    email = models.EmailField(blank=True);
    vat_p_iva = models.CharField(max_length=20, blank=True);

#non so se devo scrivere altro
#questo è per stampare l'indirizzo delle scuole di danza
def full_address(self):
    return f"{self.street},  {self.zipcode}, {self.city} ({self.id})"

#questo è per stampare i nomi delle scuole di danza
def __str__(self) -> str:        
    return self.name