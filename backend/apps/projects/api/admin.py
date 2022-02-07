from django.contrib import admin

from apps.projects.api.models import Api, Suite, RpcItem, RpcRecord


# Register your models here.

class ApiAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class SuiteAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class RpcItemAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class RpcRecordAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


admin.site.register(Api, ApiAdmin)
admin.site.register(Suite, SuiteAdmin)
admin.site.register(RpcItem, RpcItemAdmin)
admin.site.register(RpcRecord, RpcRecordAdmin)

