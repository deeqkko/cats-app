from django.contrib import admin
from cats.models import Cats


class CatsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cats, CatsAdmin)
