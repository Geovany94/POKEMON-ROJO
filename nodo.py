
class Nodo:
    def __init__(self, nivel, id, nombre, apodo, xp, tipo, movimiento, stat):
        self.nivel = nivel
        self.id = id
        self.nombre = nombre
        self.apodo = apodo
        self.xp = xp
        self.tipo = tipo
        self.movimientos = movimiento
        #Datos de combate
        self.stat = stat
        
        self.siguiente = None

    def __str__(self):
        return str(f"\n \tLa id es: {self.id}\n \tnombre: {self.nombre}\n \tel apodo es: {self.apodo}\n \tsu nivel: {self.nivel}\n \tSu experiencia es: {self.xp}\n \tEl tipo es: {self.tipo}\n \tsus movimientos son: {self.movimientos}\n \ty sus stats son {self.stat}\n\n")