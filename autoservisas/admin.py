from django.contrib import admin

from . models import Automobilio_modelis, Automobilis, Uzsakymas, Paslauga, Uzsakymoeilutes



class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'automobilio_mod_id', 'valstybiniai_nr', 'vin')
    list_filter = ('klientas',)
    search_fields = ('valstybiniai_nr', 'vin')

class Automobilio_modelisAdmin(admin.ModelAdmin):
    list_display = ('modelis',)


class UzsakymoeilutesInline(admin.TabularInline):
    model = Uzsakymoeilutes
    extra = 0

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')
    search_fields = ('pavadinimas',)

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'suma')
    list_filter = ('data',)
    list_editable = ('suma', 'data')
    search_fields = ('id', 'automobilis__klientas', 'automobilis__valstybiniai_nr')
    inlines = [UzsakymoeilutesInline]



admin.site.register(Automobilio_modelis, Automobilio_modelisAdmin)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymoeilutes)
# Register your models here.
