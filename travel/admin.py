from django.contrib import admin
from .models import Travel, UTravel




@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('t_id', 'u_id', 'yeb_event', 'from_location', 'to_location', 'amount')
    search_fields = ('yeb_event', 'from_location', 'to_location')

@admin.register(UTravel)
class UTravelAdmin(admin.ModelAdmin):
    list_display = ('u_id', 't_id')