from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



#class Profile(models.Model):
  #  user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  favorites = models.ManyToManyField('Tovar', related_name='favorited_by')

  #  def __str__(self):
   #     return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Дополнительные поля профиля

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Tovar(models.Model):
    opis = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=50)
    skidka = models.FloatField(default=1)
    category = models.CharField(max_length=50, blank=True, null=True)

class Korzina(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)

    def calcSumma(self):
        return self.count * self.tovar.price * self.tovar.skidka

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
class YourModel(models.Model):

    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()







