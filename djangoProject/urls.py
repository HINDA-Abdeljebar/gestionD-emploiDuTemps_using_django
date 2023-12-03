"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from scheduleManagement import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #users
    path('users_home/', views.user_home),
    path('add_utilisateur/', views.add_utilisateur, name='add_utilisateur'),
    path('users_list/', views.list_utilisateurs, name='users_list'),
    #cours
    path('cours_home/', views.cours_home),
    path('add_cours/', views.add_cours, name='add_cours'),
    path('cours_list/', views.cours_list, name='cours_list'),
    #salle
    path('salle_home/', views.salle_home),
    path('add_salle/', views.add_salle, name='add_salle'),
    path('salles_list/', views.salle_list, name='salles_list'),
    #emploi du temps
    path('emploi_home/', views.emlpoi_home),
    path('add_emploi/', views.add_emploi_du_temps, name='add_emploi'),
    path('emploi_list/', views.emploi_list, name='emploi_list'),
    



    



]
