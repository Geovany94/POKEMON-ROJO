

class Datos:
    def __init__(self, nivel, ps, psindividual):
        self.vi = psindividual
        self.eb = ps
        self.n = nivel
        self.a= None
        
    
    def puntos_salud(self):
        lineal= (self.vi + 2 *self.eb)*(self.n/100) + 10 +self.n
        return lineal
        
    def datos_combate(self):
        datos_com= (self.vi + 2 *self.eb)*(self.n/100) + 5
        return datos_com

    def daños_punto_salud():
        pass

    def huir_del_combate():
        pass

    def capturar_pokemon_sal():
        pass

    def aprendizaje_de_movimientos():
        pass

    def bonificacion_monetaria():
        pass
    
    