from modulos.cliente import Cliente

class ClientePlus(Cliente):
    def __init__(self, nombre: str, apellido: str, correo_electronico: str, direccion: str, descuento: float):
        super().__init__(nombre, apellido, correo_electronico, direccion)
        self.descuento = descuento

    def aplicar_descuento(self, precio: float) -> float:
        descuento_aplicado = precio * (self.descuento / 100)
        precio_final = precio - descuento_aplicado
        return precio_final