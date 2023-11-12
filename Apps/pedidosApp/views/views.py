""" Vistas de Solicitud de Pedidos """

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from Apps.pedidosApp.models import Pedido, LineaPedido
from Apps.carroApp.carro import Carro
# Para envio de e-mail
from Apps.pywebApp.views.v_email  import envio_email

@login_required(login_url="/autenticaApp/logear")
def procesar_pedido(request):
    """ función para grabar pedido """
    usuario = request.user
    pedido = Pedido.objects.create(user = usuario)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)
    asunto = "Gracias por el pedido"
    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombreusuario = request.user.username,
        emailusuario = request.user.email,
        asunto = asunto
    )
    messages.success(request, "El pedido se ha creado correctamente")
    return redirect("../tienda")

def enviar_mail(**kwargs):
    """ función para envio por email el pedido """
    asunto = kwargs.get("asunto")
    mensaje = render_to_string(
        "emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido":  kwargs.get("lineas_pedido"),
        "nombreusuario":  kwargs.get("nombreusuario"),
    })
    mensaje_texto = strip_tags(mensaje) # elimina etiquetas de variable mensaje
    from_email = "marcolecona@gmail.com"
    destinatario =  kwargs.get("emailusuario")
    
    valores = {"destinatario": destinatario, 
                      "asunto": asunto,
                      "email": from_email,
                      "mensaje": mensaje_texto}
    email = envio_email.envioemail(**valores) 
    if email:
        print("email enviado: valido")
        #return redirect("/contacto/?valido")
    else:
        print("email enviado: NO valido")
        #return redirect("/contacto/?novalido")
