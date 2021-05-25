from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, RegModelForm
from .models import Registrado, Contacto

# Create your views here.
def inicio(request):
    titulo = "Bienvenido"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)

    context = {
        "titulo": titulo,
        "el_form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        form_data = form.cleaned_data
        nombre = form_data.get('nombre')
        email = form_data.get('email')
        if not instance.nombre:
            instance.nombre = "PERSONA"
        instance.save()

        context = {
            "titulo":"Gracias %s!"%(nombre)
        }

        if not nombre:
            context = {
            "titulo":"Gracias %s!"%(email)
            }

        print(instance)
        print(instance.timestamp)
        # form_data = form.cleaned_data
        # form_name = form_data.get('nombre')
        # form_email = form_data.get('email')
        # obj = Registrado.objects.create(email=form_email, nombre=form_name)
    if request.user.is_authenticated and request.user.is_staff:
        queryset = Registrado.objects.all().order_by("-timestamp") #.filter(nombre__iexact="edgar")
            
        context = {
            "queryset": queryset
        }
        
    
    return render(request, "inicio.html", context)

def contact(request):
    titulo = "Formulario de contacto"
    form = ContactForm(request.POST or None)

    context = {
        "titulo": titulo,
        "form": form,
    }
    if form.is_valid():
        # for key, valor in form.cleaned_data.items():
        #     print(f"{key}: {valor}")
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = "Form de contacto"
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "laadriis@gmail.com"]
        mensaje_email = f"{form_nombre}:{form_mensaje} enviado por {form_email}"
        send_mail(
            asunto,
            mensaje_email,
            email_from,
            [email_to],
            fail_silently=False
        )
        # print(email, mensaje, nombre)
    
    return render(request, "forms.html", context)