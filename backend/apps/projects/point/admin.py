from django.contrib import admin

from apps.projects.point.models import Point, Suite


# Register your models here.

class PointAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class SuiteAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


admin.site.register(Point, PointAdmin)
admin.site.register(Suite, SuiteAdmin)

