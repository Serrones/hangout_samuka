from django.contrib import admin #já vem default
from petshop.models import Animal, Dono, Funcionario, Atendimento #importando minhas classes models

# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display= ('nome', 'tipo', 'dono')

class DonoAdmin(admin.ModelAdmin):
    list_display= ('nome', 'tel')

class FuncAdmin(admin.ModelAdmin):
    list_display= ('nome', 're')

class AtendAdmin(admin.ModelAdmin):
    list_display= ('animal', 'responsavel', 'consulta','campo_obs')

    def campo_obs(self, obj):
        return obj.observacao[:30]
    campo_obs.short_description = "observacao encurtada"

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Dono, DonoAdmin)
admin.site.register(Funcionario, FuncAdmin)
admin.site.register(Atendimento, AtendAdmin)
