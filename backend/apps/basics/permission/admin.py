from django.contrib import admin

from apps.basics.permission.models import Menu, UserProfile, Dept, Post, Role


# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class UserProfileAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class DeptAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class RoleAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


class PostAdmin(admin.ModelAdmin):
    excluded = ('update_datetime', 'description')
    list_per_page = 20


admin.site.register(Menu, MenuAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Post, PostAdmin)

