from django.shortcuts import render,redirect ,get_object_or_404
from .models import Deskovka, Zanr, Rozsireni, Tvurci
from .forms import UserRegistrationForm, BoardModelForm, ZanrForm, RozsireniForm, TvurciForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

class DeskovkaCreationView(CreateView):
    model = Deskovka
    form_class = BoardModelForm
    template_name = 'games/boardgames_list.html'

    def get_success_url(self):
        return reverse_lazy('deskovka_detail', kwargs={'pk': self.object.pk})


class DeskovkaListView(ListView):
    model = Deskovka
    template_name = 'games/boardgames_list.html'
    queryset = Deskovka.objects.order_by('nazev')
    context_object_name = 'deskovky'

class DeskovkaDetailView(DetailView):
    model = Deskovka
    template_name = 'games/boardgames_detail.html'
    context_object_name = 'deskovka'

def create_deskovka(request):
    if request.method == 'POST':
        form = BoardModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('deskovka_list')
    else:   
        form = BoardModelForm()

    return render(request, 'games/boardgames_create.html', {'form': form})
        
def upadate_deskovka(request, pk):
    deskovka = get_object_or_404(Deskovka, pk=pk)
    if request.method == 'POST':
        form = BoardModelForm(request.POST, request.FILES, instance=deskovka)
        if form.is_valid():
            form.save()
            return redirect('deskovka_detail', pk=deskovka.pk)
    else:
        form = BoardModelForm(instance=deskovka)

    return render(request, 'games/boardgames_update.html', {'form': form, 'deskovka': deskovka})

def delete_deskovka(request, pk):
    deskovka = get_object_or_404(Deskovka, pk=pk)
    if request.method == 'POST':
        deskovka.delete()
        return redirect('deskovka_list')
    return render(request, 'games/boardgames_delete.html', {'deskovka': deskovka})

class ZanrListView(ListView):
    model = Zanr
    template_name = 'genre/genre_list.html'
    context_object_name = 'zanry'

def zanr_detail(request, pk):
    zanr = get_object_or_404(Zanr, pk=pk)
    return render(request, 'genre/genre_detail.html', {'zanr': zanr})



def zanr_delete(request, pk):
    zanr = get_object_or_404(Zanr, pk=pk)
    if request.method == 'POST':
        zanr.delete()
        return redirect('zanr_list')
    return render(request, 'genre/genre_delete.html', {'zanr': zanr})

def zanr_create(request):
    if request.method == 'POST':
        form = ZanrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zanr_list')
    else:
        form = ZanrForm()
    return render(request, 'genre/genre_create.html', {'form': form})

class RozsireniListView(ListView):
    model = Rozsireni
    template_name = 'expansions/expansion_list.html'
    context_object_name = 'rozsireni'



def rozsireni_create(request):
    if request.method == 'POST':
        form = RozsireniForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rozsireni_list')
    else:
        form = RozsireniForm()
    return render(request, 'expansions/expansion_create.html', {'form': form})

def rozsireni_detail(request, pk):
    rozsireni = get_object_or_404(Rozsireni, pk=pk)
    return render(request, 'expansions/expansion_detail.html', {'rozsireni': rozsireni})

def rozsireni_update(request, pk):
    rozsireni = get_object_or_404(Rozsireni, pk=pk)
    if request.method == 'POST':
        form = RozsireniForm(request.POST, request.FILES, instance=rozsireni)
        if form.is_valid():
            form.save()
            return redirect('rozsireni_detail', pk=rozsireni.pk)
    else:
        form = RozsireniForm(instance=rozsireni)
    return render(request, 'expansions/expansion_update.html', {'form': form, 'rozsireni': rozsireni})

def rozsireni_delete(request, pk):
    rozsireni = get_object_or_404(Rozsireni, pk=pk)
    if request.method == 'POST':
        rozsireni.delete()
        return redirect('rozsireni_list')
    return render(request, 'expansions/expansion_delete.html', {'rozsireni': rozsireni})

def tvurci_list(request):
    role = request.GET.get('role')  # např. 'designer'
    tvurci = Tvurci.objects.all().order_by('Jmeno')

    if role:
        tvurci = tvurci.filter(role=role)

    # Předáme i seznam všech dostupných rolí (ze `ROLE_CHOICES`)
    role_choices = dict(Tvurci.ROLE_CHOICES)

    return render(request, 'tvurci/tvurci_list.html', {
        'tvurci': tvurci,
        'role': role,
        'role_choices': role_choices,
    })


def tvurci_create(request):
    if request.method == 'POST':
        form = TvurciForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tvurci_list')
    else:
        form = TvurciForm()
    return render(request, 'tvurci/tvurci_create.html', {'form': form})

def tvurci_detail(request, pk):
    tvurce = get_object_or_404(Tvurci, pk=pk)
    return render(request, 'tvurci/tvurci_detail.html', {'tvurce': tvurce})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        }
    return render(request, 'users/register.html', context=context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
            
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/dashboard.html')
    else:
        return redirect('login')