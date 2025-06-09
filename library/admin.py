from django.contrib import admin
from .models import Deskovka, Zanr, Rozsireni, Vydavatelstvi, Tvurci, Role

# Register your models here.
admin.site.register(Deskovka)
admin.site.register(Zanr)
admin.site.register(Rozsireni)
admin.site.register(Vydavatelstvi)
admin.site.register(Tvurci)
admin.site.register(Role)