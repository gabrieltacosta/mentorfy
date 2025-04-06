from django.contrib import admin
from .models import Mentorados, Navigators, DisponibilidadeHorarios, Reuniao, Tarefa, Upload

# Register your models here.
admin.site.register(Mentorados)
admin.site.register(Navigators)
admin.site.register(DisponibilidadeHorarios)
admin.site.register(Reuniao)
admin.site.register(Tarefa)
admin.site.register(Upload)
