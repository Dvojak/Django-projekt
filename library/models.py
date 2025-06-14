from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# Create your models here.


class Deskovka(models.Model):
    nazev = models.CharField(max_length=80, verbose_name="Jméno deskové hry", help_text="Zadejte jméno deskové hry", default='',
            error_messages={'blank':'Jméno deskové hry musí být vyplněno'})
    alt = models.CharField(max_length=80, verbose_name="Alternativní jméno deskové hry", help_text="Zadejte alternativní jméno deskové hry",default='')
    zanry = models.ManyToManyField('Zanr',related_name='deskovky',verbose_name='Žánry deskové hry',help_text='Vyberte jeden nebo více žánrů',blank=True)
    vydani = models.IntegerField(blank=True,null=True, verbose_name='Datum vydání', validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    minvek = models.IntegerField(verbose_name='Minimální věk', help_text='Zadejte minimální věk', validators=[MinValueValidator(0), MaxValueValidator(99)],default=0)
    cas = models.IntegerField(verbose_name='Délka hry', help_text='Zadejte délku hry v minutách', validators=[MinValueValidator(0), MaxValueValidator(999)], default=0)
    min_hracu = models.IntegerField(verbose_name='Minimální počet hráčů', help_text='Zadejte minimální počet hráčů', validators=[MinValueValidator(1), MaxValueValidator(99)],default=1)
    max_hracu = models.IntegerField(verbose_name='Maximální počet hráčů', help_text='Zadejte maximální počet hráčů', validators=[MinValueValidator(1), MaxValueValidator(99)],default=1)
    KOMPLEXITA = [(0, ''), (1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'), ]
    komplexita = models.PositiveIntegerField(choices=KOMPLEXITA, verbose_name="Komplexita hry", default=3)
    fotografie = models.ImageField(upload_to='deskovky',verbose_name='Fotografie',blank=True,null=True)
    popis = models.TextField(verbose_name='Popis', help_text='Zadejte popis deskové hry')

    class Meta:
        verbose_name = 'Deskovka'
        verbose_name_plural = 'Deskovky'

    def __str__(self):
        return f'{self.nazev},{self.alt}'



class Zanr(models.Model):
    nazev = models.CharField(max_length=20, verbose_name='Název žánru', help_text='Zadejte název žánru')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'

    def __str__(self):
        return f'{self.nazev}'


class DeskovkaZanr(models.Model):
    deskovka = models.ForeignKey(Deskovka, on_delete=models.CASCADE, related_name='deskovka_zanr')
    zanr = models.ForeignKey(Zanr, on_delete=models.CASCADE, related_name='zanr_deskovka')

    class Meta:
        verbose_name = 'Žánr deskovky'
        verbose_name_plural = 'Žánry deskovek'

    def __str__(self):
        return f'{self.deskovka.nazev} - {self.zanr.nazev}'
    

class Rozsireni(models.Model):
    nazev = models.CharField(max_length=80, verbose_name='Název rozšíření', help_text='Zadejte název rozšíření')
    deskovka = models.ForeignKey(Deskovka, on_delete=models.CASCADE, related_name='rozsirena_deskovka')
    vydani = models.IntegerField(blank=True,null=True, verbose_name='Datum vydání', validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    popis = models.TextField(verbose_name='Popis', help_text='Zadejte popis rozšíření')
    fotografie = models.ImageField(upload_to='rozsireni',verbose_name='Fotografie',blank=True,null=True)

    class Meta:
        verbose_name = 'Rozšíření'
        verbose_name_plural = 'Rozšíření'

    def __str__(self):
        return f'{self.nazev}'
    

class Vydavatelstvi(models.Model):
    Jmeno = models.CharField(max_length=80, verbose_name='Jméno vydavatelství', help_text='Zadejte jméno vydavatelství')

    class Meta:
        verbose_name = 'Vydavatelství'
        verbose_name_plural = 'Vydavatelství'

    def __str__(self):
        return f'{self.Jmeno}'

class DeskovkaVydavatelstvi(models.Model):
    deskovka = models.ForeignKey(Deskovka, on_delete=models.CASCADE, related_name='deskovka_vydavatelstvi')
    vydavatelstvi = models.ForeignKey(Vydavatelstvi, on_delete=models.CASCADE, related_name='vydavatelstvi_deskovka')

    class Meta:
        verbose_name = 'Vydavatelství deskovky'
        verbose_name_plural = 'Vydavatelství deskovek'

    def __str__(self):
        return f'{self.deskovka.nazev} - {self.vydavatelstvi.Jmeno}'



class Tvurci(models.Model):
    ROLE_CHOICES = [
        ('designer', 'Designer'),
        ('illustrator', 'Ilustrátor'),
    ]
    Jmeno = models.CharField(max_length=80, verbose_name='Jméno tvůrce', help_text='Zadejte jméno tvůrce')
    Prijmeni = models.CharField(max_length=80, verbose_name='Příjmení tvůrce', help_text='Zadejte příjmení tvůrce')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Role',blank=True, null=True, help_text='Vyberte roli tvůrce')
    zivotopis = models.TextField(verbose_name='Životopis', help_text='Zadejte životopis tvůrce', blank=True, null=True)

    class Meta:
        verbose_name = 'Tvůrce'
        verbose_name_plural = 'Tvůrci'

    def __str__(self):
        return f'{self.Jmeno} {self.Prijmeni} - ({self.get_role_display()})'
    

class DeskovkaTvurce(models.Model):
    deskovka = models.ForeignKey(Deskovka, on_delete=models.CASCADE, related_name='deskovka_tvurce')
    tvurce = models.ForeignKey(Tvurci, on_delete=models.CASCADE, related_name='tvurce_deskovka')

    class Meta:
        verbose_name = 'Tvůrce deskovky'
        verbose_name_plural = 'Tvůrci deskovek'

    def __str__(self):
        return f'{self.deskovka.nazev} - {self.tvurce.Jmeno} {self.tvurce.Prijmeni}'
    

class Hodnoceni(models.Model):
    Hra = models.ForeignKey('Deskovka', on_delete=models.CASCADE, related_name='hodnoceni_set')
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hodnoceni')
    hodnoceni = models.IntegerField(verbose_name='Hodnocení', help_text='Zadejte hodnocení', validators=[MinValueValidator(0), MaxValueValidator(10)])
    datum = models.DateField(auto_now_add=True, verbose_name='Datum hodnocení')
    recenze = models.TextField(verbose_name='Recenze', help_text='Zadejte recenzi')

    class Meta:
        verbose_name = 'Hodnocení'
        verbose_name_plural = 'Hodnocení'

    def __str__(self):
        return f'{self.Hra.nazev} - {self.uzivatel.username} - {self.hodnoceni}'


