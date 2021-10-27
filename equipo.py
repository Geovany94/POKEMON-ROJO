class Equipo:
    def __init__(self, nivel):
        self.nivel = nivel

    def equipo_poke(self, id, nombre, apodo, xp, tipo, movimientos,stat):
        self.id = id
        self.nombre = nombre
        self.apodo = apodo
        self.xp = xp
        self.tipo = tipo
        self.movimientos = movimientos
        #Datos de combate
        self.stat = stat

    def ver_pokemon():
        pass

    def batalla_pokemon():
        

    def __str__(self) -> str:
        return f"El nombre es {self.id} nombre: {self.nombre} {self.apodo} {self.nivel} {self.xp} {self.tipo} {self.movimientos} "
    