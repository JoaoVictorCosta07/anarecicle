from django.contrib import admin
from .models import Coleta, Material, Dia  # Importe seus modelos

# Registre os modelos no admin
admin.site.register(Coleta)
admin.site.register(Material)
admin.site.register(Dia)
