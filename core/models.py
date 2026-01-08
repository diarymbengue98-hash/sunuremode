from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Annonce(models.Model):
    CATEGORIES = [
        ('wax', 'Wax'),
        ('bazin', 'Bazin'),
        ('djezner', 'Djezner'),
        ('tchioup', 'Tchioup'),
        ('tissu', 'Tissu'),
    ]

    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.IntegerField()
    categorie = models.CharField(max_length=50)
    image = models.ImageField(upload_to='annonces/', blank=True, null=True)

    def __str__(self):
        return self.titre

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)

    def __str__(self):
        return f"Profil de {self.user.username}"
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)