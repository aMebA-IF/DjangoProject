from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Аватарка пользователя', null=True, blank=True, upload_to='photos/')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
    
    @property
    def places(self):
        return Place.objects.filter(profile = self)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"{self.user}"

class Place(models.Model):
    name = models.CharField(verbose_name='Имя места', null=False, max_length=50)
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)
    latitude = models.DecimalField(verbose_name='Широта', max_digits=30, decimal_places=25, null=True, blank=True)
    longitude = models.DecimalField(verbose_name='Долгота', max_digits=30, decimal_places=25, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.name

