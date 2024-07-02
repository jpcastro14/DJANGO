from django.contrib import admin

# Register your models here.

from .models import Curso,Avaliacao, Event

@admin.register(Curso)
class CursdoAdmin(admin.ModelAdmin):
    list_display = ('titulo','url','criacao','atualizacao','ativo')


@admin.register(Avaliacao)
class Avaliacao(admin.ModelAdmin):
    list_display = ('curso','nome','email','avaliacao', 'criacao', 'ativo')

@admin.register(Event)
class Event(admin.ModelAdmin):
    list_display = ('nome','local','data','technician')