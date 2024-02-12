from django.http import JsonResponse
from .models import Profile, Tovar

def add_to_favorites(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id')

        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            # Если у пользователя нет профиля, создаем его
            profile = Profile.objects.create(user=request.user)

        product = profile.add_to_favorites(product_id)

        return JsonResponse({'success': True, 'product_id': product.id})
    return JsonResponse({'success': False, 'message': 'Invalid request'})
