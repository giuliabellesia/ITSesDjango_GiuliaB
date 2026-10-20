from django.db import models

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