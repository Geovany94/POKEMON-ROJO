class Nodo_poke:
    def __init__(self, nivel, id, nombre, xp, tipo, movimiento, stat, atrapado):
        self.nivel = nivel
        self.id = id
        self.nombre = nombre
        self.xp = xp
        self.tipo = tipo
        self.movimientos = movimiento
        #Datos de combate
        self.stat = stat
        self.atrapado = atrapado
        
        self.siguiente = None

    def __str__(self):
        return str(f"\n \tLa id es: {self.id}\n \tfue atrapado: {self.atrapado}\n \tnombre: {self.nombre}\n \tsu nivel: {self.nivel}\n \tSu experiencia es: {self.xp}\n \tEl tipo es: {self.tipo}\n \tsus movimientos son: {self.movimientos}\n \ty sus stats son {self.stat}\n\n")