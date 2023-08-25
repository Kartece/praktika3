from django.contrib import admin

from . models import Automobilio_modelis, Automobilis, Uzsakymas, Paslauga, Uzsakymoeilutes



class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'valstybiniai_nr', 'vin')
    list_filter = ('klientas',)
    search_fields = ('valstybiniai_nr', 'vin')


class UzsakymoeilutesInline(admin.TabularInline):
    model = Uzsakymoeilutes
    extra = 0



class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'suma')
    list_filter = ('data',)
    list_editable = ('suma', 'data')
    search_fields = ('id', 'automobilis__klientas', 'automobilis__valstybiniai_nr')
    inlines = [UzsakymoeilutesInline]



admin.site.register(Automobilio_modelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga)
admin.site.register(Uzsakymoeilutes)
# Register your models here.
