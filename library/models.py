from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# Create your models here.


class Deskovka(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name="Jméno deskové hry", help_text="Zadejte jméno deskové hry",
            error_messages={'blank':'Jméno deskové hry musí být vyplněno'}),
    alt = models.CharField(max_length=80, verbose_name="Alternativní jméno deskové hry", help_text="Zadejte alternativní jméno deskové hry"),
    vydani = models.DateField(blank=True,null=True, verbose_name='Datum narození')
    fotografie = models.ImageField(upload_to='deskovky',verbose_name='Fotografie',blank=True,null=True)
    HODNOCENI = [(0, ''), (1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'), ]
    hodnoceni = models.PositiveIntegerField(choices=HODNOCENI, verbose_name="Průměrové hodnoceni", default=3)
    KOMPLEXITA = [(0, ''), (1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'), ]
    komplexita = models.PositiveIntegerField(choices=KOMPLEXITA, verbose_name="Komplexita hry", default=3)

    class Meta:
        verbose_name = 'Deskovka'
        verbose_name_plural = 'Deskovky'

    def __str__(self):
        return f'{self.jmeno},{self.alt}'



class Zanr(models.Model):
    nazev = models.CharField(max_length=20, verbose_name='Název žánru', help_text='Zadejte název žánru')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'

    def __str__(self):
        return f'{self.nazev}'

