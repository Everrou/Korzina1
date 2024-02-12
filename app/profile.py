from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('Tovar', related_name='favorited_by')

    def add_to_favorites(self, product):
        self.favorites.add(product)
