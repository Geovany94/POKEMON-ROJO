
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
        return str(f"\n---------------------------------------\n \tNo. en la pokedex = {self.id}\n \tNombre = {str(self.nombre).capitalize()}\n \tApodo = {self.apodo}\n \tNivel = {self.nivel}\n \tExperiencia = {self.xp}\n \tTipo = {self.tipo}\n \tMovimientos = {self.movimientos}\n \tPuntos de combate=\n\t   Ps= {self.stat[0]}\n\t   Ataque= {self.stat[1]}\n\t   Defensa = {self.stat[2]}\n\t   Ataque especial= {self.stat[3]}\n\t   Defensa especial= {self.stat[4]}\n\t   Velocidad = {self.stat[5]}\n\t\n\n")