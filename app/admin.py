from django.contrib import admin
from .models import YourModel

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Adjust the fields as needed

admin.site.register(YourModel, YourModelAdmin)