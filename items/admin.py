from django.contrib import admin
from .models import Categories
from .models import Group


class GroupInline(admin.TabularInline):
    model = Group


class CategoriesAdmin(admin.ModelAdmin):
    inlines = [
        GroupInline,
    ]


class GroupAdmin(admin.ModelAdmin):
    list_display = Group._meta.get_all_field_names()


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Group, GroupAdmin)
