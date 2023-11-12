""" Vistas de Contacto """

from django.shortcuts import render, redirect
from Apps.contactoApp.forms.forms import ContactoForm
from Apps.pywebApp.views.v_email  import envio_email

def contacto(request):
    """ función de contacto """
    formcontacto = ContactoForm()
    if request.method == "POST":
        formcontacto = ContactoForm(data=request.POST)
        if formcontacto.is_valid():
            # Datos del form
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            # Datos del form
            asunto = "Mensaje de App-Django - Gestión de Pedidos"
            mensaje = f"""Usuario:\n{nombre}\nCon E-email:\n{email}\n
                        Manda Mensaje:\n{contenido}\n Fin de Mensaje"""
            destinatario = "marcolecona@gmail.com"
            valores = {"destinatario": destinatario, 
                      "asunto": asunto,
                      "email": email,
                      "mensaje": mensaje}
            email = envio_email.envioemail(**valores) 
            if email:
                return redirect("/contacto/?valido")
            else:
                return redirect("/contacto/?novalido")
    return render(request, "contacto/contacto.html", {"miform": formcontacto})
