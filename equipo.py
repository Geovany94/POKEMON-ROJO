class Equipo:
    def __init__(self, nivel):
        self.nivel = nivel
        self.id = 5
        self.nombre = ""
        self.apodo = ""
        self.xp = 1500
        self.tipo = ""
        self.movimientos = ""
        #Datos de combate
        self.stat = ""

    def equipo_poke(self, id, nombre, apodo, xp, tipo, movimientos ,stat):
        self.id = id
        self.nombre = nombre
        self.apodo = apodo
        self.xp = xp
        self.tipo = tipo
        self.movimientos = movimientos
        #Datos de combate
        self.stat = stat

    def ver_pokemon(self):
        pass

    def generar_poke_rival(self, id, nombre, xp, tipo, movimientos,stat):
        self.id_rival = id
        self.nombre_rival = nombre
        self.xp_rival = xp
        self.tipo_rival = tipo
        self.movimientos_rival = movimientos
        #Datos de combate

        self.stat_rival = stat
        self.nivel_rival = 0 
    
    def batalla_pokemon(self):
        if self.nivel == 5:
            self.nive_rival = self.nivel - 4

        else:
            pass 



    def __str__(self) -> str:
        return f"\n La id es: {self.id}\n nombre: {self.nombre}\n el apodo es: {self.apodo}\n su nivel: {self.nivel}\n Su experiencia es: {self.xp}\n El tipo es: {self.tipo}\n sus movimientos son: {self.movimientos} "
    