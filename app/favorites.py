from django.shortcuts import render

def favorites(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Если у пользователя нет профиля, создаем его
        profile = Profile.objects.create(user=request.user)

    user_favorites = profile.favorites.all()
    return render(request, 'favorites.html', {'favorites': user_favorites})
