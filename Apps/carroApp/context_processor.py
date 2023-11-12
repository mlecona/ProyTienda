""" manejo de variable global """

def importe_carro(request):
    """ función de variable global """
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
            for key, value in request.session["carro"].items():
                total += float(value["precio"])
    else:
        total = "Debes hacer login"
    return {"importe_carro": total}
