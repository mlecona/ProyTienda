""" Clase de carro """


class Carro:
    """ clase de carro """

    def __init__(self, request):
        # Para cuando no hay inicio de sesion comenta de aquí
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        #else:
        # hast aquí terminar todo el comentario
        self.carro = carro

    def agregar(self, producto):
        """ método agregar """
        if str(producto.id) in self.carro.keys():
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] +=  1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break
        else:
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        self.guardar_carro()

    def guardar_carro(self):
        """ método para sesion de guarda carro"""
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        """ método para eliminar de carro"""
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_prod(self, producto):
        """ método para restar producto del carro"""
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -=  1
                value["precio"] = float(value["precio"]) - producto.precio
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        """ método para limpiar carro """
        self.session["carro"] = {}
        self.session.modified = True
