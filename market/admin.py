from django.contrib import admin
from gate.market.models import App

class AppAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)

admin.site.register(App, AppAdmin)
