class Equipo:
    def __init__(self, id, nombre, apodo, nivel, xp, tipo, movimientos,
        hp, ataque, defensa, ata_especial, def_especial, velocidad ):
        self.id = id
        self.nombre = nombre
        self.apodo = apodo
        self.nivel = nivel
        self.xp = xp
        self.tipo = tipo
        self.movimientos = movimientos
        #Datos de combate
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.ata_especial = ata_especial
        self.def_especial = def_especial
        self.velocidad = velocidad
    
    def ver_pokemon():
        pass
    