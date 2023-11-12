""" Vistas para envio de email """

import smtplib
from email.message import EmailMessage
from django.conf import settings


class envio_email:

    def envioemail(**kwargs):
        """ funcion de Envio Email """
        # datos base en settings
        remitente = settings.EMAIL_HOTS_USER
        password = settings.EMAIL_HOST_PASSWORD
        emailhost = settings.EMAIL_HOTS
        # Se obtienen datos de email
        email = kwargs.get("email")
        asunto = kwargs.get("asunto")
        mensaje = kwargs.get("mensaje")
        destinatario = kwargs.get("destinatario")
        # armando email
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = asunto
        email.set_content(mensaje)
        smtp = smtplib.SMTP_SSL(emailhost)
        smtp.login(remitente, password)
        try:
            smtp.sendmail(remitente, destinatario, email.as_string())
            smtp.quit()
            return True
        except Exception as e:
            return False
