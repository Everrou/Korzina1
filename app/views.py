
from django.shortcuts import render, redirect
from .models import *

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView






def index(req):

    items = Tovar.objects.exclude(id=1)
    data = {'tovari': items}
    return render(req, 'index.html', data)


def buy(req,id):
    item = Tovar.objects.get(id=id)
    if Korzina.objects.filter(tovar_id=id):
        getTovar = Korzina.objects.get(tovar_id=id)
        getTovar.count+=1
        getTovar.summa = getTovar.calcSumma()
        getTovar.save()
    else:
        Korzina.objects.create(count=1, tovar=item, summa=item.price)
    return redirect('toKorz')

def toKorz(req):
    items = Korzina.objects.all()
    itog = 0
    for i in items:
        itog+=i.summa

    data = {'items':items,'itog':itog}
    return render(req, 'korzina.html', data)


def delete(req,id):
    item = Korzina.objects.get(id=id)
    item.delete()
    return redirect('toKorz')

def korzinaZakaz(req):
    print('doshel',adres)
    if req.POST:
        data = req.POST
        print(data)

    return HttpResponse('Спасибо за заказ!')
    #return redirect('home')
from django.shortcuts import render




def favorites(request):
    user_profile = request.user.profile if hasattr(request.user, 'profile') else None

    if user_profile:
        user_favorites = user_profile.favorites.all()
        return render(request, 'favorites.html', {'favorites': user_favorites})
    else:
        return JsonResponse({'error': 'User profile not found'}, status=400)

#def profile(request):

  #  return render(request, 'profile.html')  # Создайте файл profile.html в папке templates

def contact(request):
    # Ваш код для страницы связи
    return render(request, 'contact.html')  # Создайте файл contact.html в папке templates

def cakes(request):
    excluded_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    items = Tovar.objects.filter(id__in=excluded_ids)  # Замените 1 на фактический id товара
    data = {'tovari': items}
    return render(request, 'cakes.html', data)

def cakes2 (request):
    excluded_ids = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    items = Tovar.objects.filter(id__in=excluded_ids)
    data = {'tovari': items}
    return render(request, 'cakes2.html', data)

def cakes3 (request):
    excluded_ids = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    items = Tovar.objects.filter(id__in=excluded_ids)
    data = {'tovari': items}
    return render(request, 'cakes3.html', data)

def cakes4 (request):
    excluded_ids = [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
    items = Tovar.objects.filter(id__in=excluded_ids)
    data = {'tovari': items}
    return render(request, 'cakes4.html', data)

def cakes5 (request):
    excluded_ids = [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]
    items = Tovar.objects.filter(id__in=excluded_ids)
    data = {'tovari': items}
    return render(request, 'cakes5.html', data)

def cakes6 (request):
    excluded_ids = [83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]
    items = Tovar.objects.filter(id__in=excluded_ids)
    data = {'tovari': items}
    return render(request, 'cakes6.html', data)

def cakes7 (request):
    excluded_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    items = Tovar.objects.filter(id__in=excluded_ids)
    data = {'tovari': items}
    return render(request, 'cakes7.html', data)

def cakes8 (request):
    excluded_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    items = Tovar.objects.filter(id__in=excluded_ids)
    data = {'tovari': items}
    return render(request, 'cakes8.html', data)

def cakes9 (request):
    excluded_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    items = Tovar.objects.filter(id__in=excluded_ids)
    data = {'tovari': items}
    return render(request, 'cakes9.html', data)























def profile(request):
    try:
        user_profile = request.user.profile if hasattr(request.user, 'profile') else None
        if user_profile:
            # Ваш код для работы с профилем пользователя
            return render(request, 'profile.html', {'user_profile': user_profile})
        else:
            return JsonResponse({'error': 'User profile not found'}, status=400)
    except Exception as e:
        logger.error(f"Error in profile view: {e}")
        return JsonResponse({'error': 'Internal server error'}, status=500)

























