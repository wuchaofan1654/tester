from django.contrib import admin

from apps.projects.efficiency.models import Efficiency, Module


# Register your models here.

class EfficiencyAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


# class ModuleAdmin(admin.ModelAdmin):
#     excluded = ('update_datetime', 'description')
#     list_per_page = 20


admin.site.register(Efficiency, EfficiencyAdmin)
admin.site.register(Module)

