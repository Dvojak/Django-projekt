from django.shortcuts import render,redirect ,get_object_or_404
from .models import Deskovka, Zanr, Rozsireni
from .forms import UserRegistrationForm, BoardModelForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'users/index.html')

class DeskovkaCreationView(CreateView):
    model = Deskovka
    form_class = BoardModelForm
    template_name = 'templates/games/boardgames_list.html'

    def get_success_url(self):
        return reverse_lazy('deskovka_detail', kwargs={'pk': self.object.pk})


class DeskovkaListView(ListView):
    model = Deskovka
    template_name = 'templates/games/boardgames_list.html'
    queryset = Deskovka.objects.order_by('nazev')
    context_object_name = 'deskovky'

class DeskovkaDetailView(DetailView):
    model = Deskovka
    template_name = 'templates/games/boardgames_detail.html'
    context_object_name = 'deskovka'

class DeskovkaUpdateView(UpdateView):
    model = Deskovka
    form_class = BoardModelForm
    template_name = 'templates/games/boardgames_update.html'

    def get_success_url(self):
        return reverse_lazy('deskovka_detail', kwargs={'pk': self.object.pk})


class DeskovkaDeleteView(DeleteView):
    model = Deskovka
    template_name = 'templates/games/boardgames_delete.html'
    context_object_name = 'deskovka'
    success_url = reverse_lazy('deskovka_list')

def books_by_genre(request, genre):
    if not Zanr.objects.filter(nazev=genre).exists():
        return render(request, '404.html',status=404)
    context = {
        'genre': genre,
        'deskovky': Deskovka.objects.order_by('nazev').filter(zanr__zanr=genre),
    }
    return render(request,'templates/games/boardgames_by_genre.html',context=context)

def create_deskovka(request):
    if request.method == 'POST':
        form = BoardModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('deskovka_list')
    else:   
        form = BoardModelForm()

    return render(request, 'templates/games/boardgames_create.html', {'form': form})
        
def upadate_deskovka(request, pk):
    deskovka = get_object_or_404(Deskovka, pk=pk)
    if request.method == 'POST':
        form = BoardModelForm(request.POST, request.FILES, instance=deskovka)
        if form.is_valid():
            form.save()
            return redirect('deskovka_detail', pk=deskovka.pk)
    else:
        form = BoardModelForm(instance=deskovka)

    return render(request, 'templates/games/boardgames_update.html', {'form': form, 'deskovka': deskovka})

def delete_deskovka(request, pk):
    deskovka = get_object_or_404(Deskovka, pk=pk)
    if request.method == 'POST':
        deskovka.delete()
        return redirect('deskovka_list')
    return render(request, 'templates/games/boardgames_delete.html', {'deskovka': deskovka})

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