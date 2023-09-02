from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Alquileres)

admin.site.register(Venta)

admin.site.register(Inversiones)

admin.site.register(Asesores)
