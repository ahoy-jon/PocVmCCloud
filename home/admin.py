from django.contrib import admin
from gate.home.models import InstalledApp

class InstalledAppAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)

admin.site.register(InstalledApp, InstalledAppAdmin)
