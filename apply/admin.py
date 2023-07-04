from django.contrib import admin

from .models import Biodata
from .models import Contact
# Register your models here.

class BiodataAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'other_names', 'status']
    list_filter = ['status']

admin.site.register(Biodata, BiodataAdmin)
admin.site.register(Contact)