from paquetes.paquete_clientes.modulos.cliente import Cliente
from paquetes.paquete_clientes.modulos.cliente_plus import ClientePlus

def crear_cliente(nombre, apellido, email, direccion, es_premium=False, puntos_acumulados=0):

    if es_premium:
        return ClientePlus(nombre, apellido, email, direccion, puntos_acumulados)
    else:
        return Cliente(nombre, apellido, email, direccion)

def main():
    # Crear clientes de ejemplo
    cliente1 = crear_cliente("Paola", "Bordon", "p.bordon@example.com", "Calle 1234")
    cliente2 = crear_cliente("Matias", "Werjman", "m.werjman@example.com", "Aven 1234")