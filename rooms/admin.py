from django.contrib import admin

from .models import Reservation, Salle


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 1


class SalleAdmin(admin.ModelAdmin):
    inlines = [ReservationInline]
    list_display = ('nom', 'ressource_type', 'localisation','capacite')
    search_fields = ['nom']
    
admin.site.register(Salle, SalleAdmin)
