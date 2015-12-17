from django.contrib import admin
from .models import Ruangan, Kategori, Peralatan


class PeralatanInline(admin.TabularInline):
    model = Peralatan
    extra = 0


class KategoriAdmin(admin.ModelAdmin):
    inlines = [PeralatanInline]


# Register your models here.
admin.site.register(Ruangan)
admin.site.register(Kategori, KategoriAdmin)
