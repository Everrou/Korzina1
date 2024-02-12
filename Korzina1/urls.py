
from django.contrib import admin
from django.urls import path
from app import views
from app.views import profile





urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('cart/<int:id>', views.buy, name='buy'),
    path('cart/', views.toKorz, name='toKorz'),
    path('cart/del/<int:id>', views.delete, name='del'),
    path('cart/pobeda/<str:adres>', views.korzinaZakaz, name='korzinaZakaz'),
    path('cakes/', views.cakes, name='cakes'),
    path('cakes2/', views.cakes2, name='cakes2'),  # Исправлено
    path('cakes3/', views.cakes3, name='cakes3'),  # Исправлено
    path('cakes4/', views.cakes4, name='cakes4'),  # Исправлено
    path('cakes5/', views.cakes5, name='cakes5'),  # Исправлено
    path('cakes6/', views.cakes6, name='cakes6'),
    path('cakes7/', views.cakes7, name='cakes7'),
    path('cakes8/', views.cakes8, name='cakes8'),
    path('cakes9/', views.cakes9, name='cakes9'),







    path('favorites/', views.favorites, name='favorites'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('profile/', profile, name='profile'),



]

