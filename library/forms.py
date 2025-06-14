from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deskovka, Zanr, Rozsireni, Tvurci


class BoardModelForm(forms.ModelForm):
    class Meta:
        model = Deskovka
        fields = [ 'nazev', 'alt','designer','zanry', 'vydani', 'minvek', 'cas',
            'min_hracu', 'max_hracu', 'komplexita', 'fotografie', 'popis']
        labels = {
            'nazev': 'Název hry',
            'alt': 'Alternativní název',
            'designer': 'Jméno tvůrce/ců',
            'zanry': 'Žánr/y',
            'vydani': 'Rok vydání',
            'minvek': 'Minimální věk',
            'cas': 'Délka hry (min)',
            'min_hracu': 'Min. hráčů',
            'max_hracu': 'Max. hráčů',
            'komplexita': 'Komplexita',
            'fotografie': 'Obrázek',
            'popis': 'Popis hry',
        }
        help_texts = {
            'nazev': 'Zadejte jméno deskové hry',
            'alt': 'Zadejte alternativní jméno deskové hry',
            'designer': 'Vyberte jméno tvůrce/ců hry',
            'zanry': 'Vyberte žánr či žánry deskové hry',
            'rok_vydani': 'Zadejte rok vydání deskové hry',
            'minimalni_vek': 'Zadejte minimální věk',
            'prum_cas': 'Zadejte průměrnou délku hry v minutách',
            'min_hracu': 'Zadejte minimální počet hráčů',
            'max_hracu': 'Zadejte maximální počet hráčů',
            'komplexita': 'Zadejte komplexitu hry (0-5)',
            'fotografie': 'Vyberte fotografii deskové hry',
            'popis': 'Zadejte popis deskové hry',
        }
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
            'designer' : forms.CheckboxSelectMultiple(),
            'zanry': forms.CheckboxSelectMultiple(),
            'rok_vydani': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'minimalni_vek': forms.NumberInput(attrs={'class': 'form-control'}),
            'prum_cas': forms.NumberInput(attrs={'class': 'form-control'}),
            'min_hracu': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_hracu': forms.NumberInput(attrs={'class': 'form-control'}),
            'komplexita': forms.Select(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_fotografie(self):
        fotografie = self.cleaned_data.get('fotografie')
        if fotografie:
            if not fotografie.name.endswith(('.jpg', '.jpeg', '.png')):
                raise forms.ValidationError('Fotografie musí být ve formátu JPG, JPEG nebo PNG.')
        return fotografie    
        
        
class ZanrForm(forms.ModelForm):
    class Meta:
        model = Zanr
        fields = ['nazev']

class RozsireniForm(forms.ModelForm):
    class Meta:
        model = Rozsireni
        fields = ['nazev', 'deskovka', 'vydani', 'popis', 'fotografie']
        labels = {
            'nazev': 'Název rozšíření',
            'deskovka': 'Deskova hra',
            'vydani': 'Datum vydání',
            'popis': 'Popis rozšíření',
            'fotografie': 'Obrázek rozšíření',
        }
        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'vydani': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
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
    
class TvurciForm(forms.ModelForm):
    class Meta:
        model = Tvurci
        fields = ['Jmeno', 'Prijmeni', 'role', 'zivotopis', 'fotografie']
        labels = {
            'Jmeno': 'Jméno tvůrce',
            'Prijmeni': 'Příjmení tvůrce',
            'role': 'Role tvůrce',
            'zivotopis': 'Životopis',
            'fotografie': 'Fotografie',
        }
        widgets = {
            'Jmeno': forms.TextInput(attrs={'class': 'form-control'}),
            'Prijmeni': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'zivotopis': forms.Textarea(attrs={'class': 'form-control'}),
            'fotografie': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_fotografie(self):
        fotografie = self.cleaned_data.get('fotografie')
        if fotografie:
            ext = fotografie.name.lower().split('.')[-1]
            if ext not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError('Fotografie musí být ve formátu JPG, JPEG nebo PNG.')
        return fotografie