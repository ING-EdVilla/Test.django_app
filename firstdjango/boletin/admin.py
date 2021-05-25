from django.contrib import admin
from .forms import RegModelForm, ContactForm
# Register your models here.
from .models import Registrado, Contacto

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre", "timestamp"]
    form = RegModelForm
    # list_display_links = ["nombre"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]
    # class Meta:
    #     model = Registrado


class AdminContacto(admin.ModelAdmin):
    list_display = ["email", "nombre", "mensaje", "timestamp"]
    form = ContactForm
    # list_display_links = ["nombre"]
    list_filter = ["nombre"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]
    # class Meta:
    #     model = Registrado


admin.site.register(Registrado, AdminRegistrado)
admin.site.register(Contacto, AdminContacto)