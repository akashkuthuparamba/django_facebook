from django.contrib import admin
from . models import Log_in,Profile

# Register your models here.
class Log_inAdmin(admin.ModelAdmin):
    list_display = ['username', 'place','phone_no']



admin.site.register(Log_in)
