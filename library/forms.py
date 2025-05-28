from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deskovka, Zanr, Rozsireni


class BoardModelForm(forms.ModelForm):
    class Meta:
        model = Deskovka
        fields = ['nazev','alt', 'vydani', 'minvek','cas','pocet_hrac','komplexita','fotografie','popis']
        labels = {
            'nazev': 'Jméno deskové hry',
            'alt': 'Alternativní jméno deskové hry',
            'rok_vydani': 'Rok vydání',
            'minimalni_vek': 'Minimální věk',
            'prum_cas': 'Průměrná délka hry',
            'pocet_hracu': 'Počet hráčů',
            'komplexita': 'Komplexita hry',
            'fotografie': 'Fotografie',
            'popis': 'Popis',
        }
        help_texts = {
            'nazev': 'Zadejte jméno deskové hry',
            'alt': 'Zadejte alternativní jméno deskové hry',
            'rok_vydani': 'Zadejte rok vydání deskové hry',
            'minimalni_vek': 'Zadejte minimální věk',
            'prum_cas': 'Zadejte průměrnou délku hry v minutách',
            'pocet_hracu': 'Zadejte počet hráčů',
            'komplexita': 'Zadejte komplexitu hry (0-5)',
            'fotografie': 'Vyberte fotografii deskové hry',
            'popis': 'Zadejte popis deskové hry',
        }
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
            'rok_vydani': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'minimalni_vek': forms.NumberInput(attrs={'class': 'form-control'}),
            'prum_cas': forms.NumberInput(attrs={'class': 'form-control'}),
            'pocet_hracu': forms.NumberInput(attrs={'class': 'form-control'}),
            'komplexita': forms.Select(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_fotografie(self):
        fotografie = self.cleaned_data.get('fotografie')
        if fotografie:
            if not fotografie.name.endswith(('.jpg', '.jpeg', '.png')):
                raise forms.ValidationError('Fotografie musí být ve formátu JPG, JPEG nebo PNG.')
        return fotografie    
        




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user