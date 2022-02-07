from django.contrib import admin

from apps.projects.case.models import Case, Suite, Record


# Register your models here.

class CaseAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class SuiteAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class RecordAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


admin.site.register(Case, CaseAdmin)
admin.site.register(Suite, SuiteAdmin)
admin.site.register(Record, RecordAdmin)

