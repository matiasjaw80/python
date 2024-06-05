class Cliente:
    def __init__(self, nombre, apellido, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Correo electrónico: {self.email}")
        print(f"Dirección: {self.direccion}")

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email