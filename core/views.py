from django.shortcuts import render, redirect, get_object_or_404
from .models import Annonce
from .forms import AnnonceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Annonce, Profil
from .forms import ProfilForm
from .models import Profil, Annonce
from django.contrib import messages
def home(request):
    annonces = Annonce.objects.all().order_by('-id')
    return render(request, 'core/home.html', {'annonces': annonces})


def cgu(request):
    return render(request, 'core/cgu.html')


def confidentialite(request):
    return render(request, 'core/confidentialite.html')


def mentions(request):
    return render(request, 'core/mentions.html')


def categorie(request, type_vetement):
    annonces = Annonce.objects.filter(categorie=type_vetement)
    return render(request, 'core/categorie.html', {
        'type_vetement': type_vetement,
        'annonces': annonces
    })

@login_required
def publier_annonce(request):
    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES)
        if form.is_valid():
            annonce = form.save(commit=False)
            annonce.auteur = request.user
            annonce.save()
            return redirect('home')
    else:
        form = AnnonceForm()

    return render(request, 'core/publier_annonce.html', {'form': form})

def detail_annonce(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id)
    return render(request, 'core/detail_annonce.html', {'annonce': annonce})

@login_required
def mes_annonces(request):
    annonces = Annonce.objects.filter(auteur=request.user)
    return render(request, 'core/mes_annonces.html', {
        'annonces': annonces
    })

@login_required
def modifier_annonce(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id, auteur=request.user)

    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES, instance=annonce)
        if form.is_valid():
            form.save()
            return redirect('mes_annonces')
    else:
        form = AnnonceForm(instance=annonce)

    return render(request, 'core/publier_annonce.html', {'form': form})

@login_required
def supprimer_annonce(request, annonce_id):
    annonce = get_object_or_404(Annonce, id=annonce_id, auteur=request.user)

    if request.method == 'POST':
        annonce.delete()
        return redirect('mes_annonces')

    return render(request, 'core/supprimer_annonce.html', {
        'annonce': annonce
    })
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profil(request):
    profil, created = Profil.objects.get_or_create(user=request.user)
    annonces = Annonce.objects.filter(auteur=request.user)

    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil mis à jour avec succès")
            return redirect('profil')
    else:
        form = ProfilForm(instance=profil)

    return render(request, 'core/profil.html', {
        'profil': profil,
        'form': form,
        'annonces': annonces
    })
