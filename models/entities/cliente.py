class Cliente:
    def __init__(self, cedula, nombre, whatsapp, email): #constructor
        self.cedula = cedula
        self.nombre = nombre
        self.whatsapp = whatsapp
        self.email = email

    def to_JSON(self): #aqui retornaremos un JSON con los datos
        return {
            'cedula' : self.cedula,
            'name' : self.nombre,
            'whatsapp' : self.whatsapp,
            'email' : self.email
        }
