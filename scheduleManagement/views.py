from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# users
def user_home(request):
    return render(request , 'scheduleManagement/user/add_user.html')

def add_utilisateur(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        role = request.POST.get('role')
        email = request.POST.get('email')

        if nom and prenom and role and email:
            new_user = Utilisateur.objects.create(
                nom=nom,
                prenom=prenom,
                role=role,
                email=email
            )
            return HttpResponseRedirect('/users_list')  

    return render(request, '/add_utilisateur')


def list_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()  # Fetch all users
    return render(request, 'scheduleManagement/user/user_list.html', {'utilisateurs': utilisateurs})

#cours
def cours_home(request):
    return render(request , 'scheduleManagement/cours/add_cours.html')

def add_cours(request):
    if request.method == 'POST':
        nom_cours = request.POST.get('nom_cours')
        description = request.POST.get('description')

        if nom_cours and description:
            new_course = Cours.objects.create(
                nom_cours=nom_cours,
                description=description
            )
            return HttpResponseRedirect('/cours_list')  

    return render(request, 'scheduleManagement/cours/add_cours.html')


def cours_list(request):
    cours = Cours.objects.all() 
    return render(request, 'scheduleManagement/cours/cours_list.html', {'cours': cours})


#salle
def salle_home(request):
    return render(request , 'scheduleManagement/salle/add_salle.html')


def add_salle(request):
    if request.method == 'POST':
        nom_salle = request.POST.get('nom_salle')
        capacite = request.POST.get('capacite')

        if nom_salle and capacite:
            new_salle = Salle.objects.create(
                nom_salle=nom_salle,
                capacite=capacite
            )
            return HttpResponseRedirect('/salles_list/') 

    return render(request, 'scheduleManagement/salle/add_salle.html')


def salle_list(request):
    salles = Salle.objects.all() 
    return render(request, 'scheduleManagement/salle/salle_list.html', {'salles': salles})


# emploi su temps
def emlpoi_home(request):
    return render(request , 'scheduleManagement/emploiDuTemps/add_emploi.html')

def add_emploi_du_temps(request):
    if request.method == 'POST':
        jour_semaine = request.POST.get('jour_semaine')
        heure_debut = request.POST.get('heure_debut')
        heure_fin = request.POST.get('heure_fin')
        cours_id = request.POST.get('cours_id') 
        utilisateur_id = request.POST.get('utilisateur_id')  
        salle_id = request.POST.get('salle_id')  

        if jour_semaine and heure_debut and heure_fin and cours_id and utilisateur_id and salle_id:
            new_emploi = EmploiDuTemps.objects.create(
                jour_semaine=jour_semaine,
                heure_debut=heure_debut,
                heure_fin=heure_fin,
                cours_id=cours_id,
                utilisateur_id=utilisateur_id,
                salle_id=salle_id
            )
            return HttpResponseRedirect('/emploi_list/')  

    return render(request, 'scheduleManagement/emploiDuTemps/add_emploi.html')

def emploi_list(request):
    emplois = EmploiDuTemps.objects.all()  
    return render(request, 'scheduleManagement/emploiDuTemps/list_emploi.html', {'emplois': emplois})

