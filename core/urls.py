from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categorie/<str:type_vetement>/', views.categorie, name='categorie'),
    path('annonce/<int:annonce_id>/', views.detail_annonce, name='detail_annonce'),
    path('mes-annonces/', views.mes_annonces, name='mes_annonces'),
    path('annonce/<int:annonce_id>/modifier/', views.modifier_annonce, name='modifier_annonce'),
    path('annonce/<int:annonce_id>/supprimer/', views.supprimer_annonce, name='supprimer_annonce'),
    path('publier/', views.publier_annonce, name='publier'),
    path('signup/', views.signup, name='signup'),
    path('profil/', views.profil, name='profil'),
    path('cgu/', views.cgu, name='cgu'),
    path('confidentialite/', views.confidentialite, name='confidentialite'),
    path('mentions/', views.mentions, name='mentions'),
]
