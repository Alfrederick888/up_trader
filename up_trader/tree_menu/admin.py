from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import *

class SubMenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(SubMenu, SubMenuAdmin)


class MenuAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Menu, MenuAdmin)
