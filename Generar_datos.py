

from lista import Mochila

mochila = Mochila()


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

class Huir:
    def __init__(self, velocidadpoke, velocidadpokesal):
        self.A = velocidadpoke
        self.B = velocidadpokesal
        
    def huir_del_combate(self):
        f=(((self.A+128)/self.B)+30)% 256
        return f


class Capturar_poke:
    def __init__(self, ps, psactual, proporcion_captura, pokeball):
        self.psmax= ps
        self.psactual= psactual
        self.Rc= proporcion_captura
        self.Rb= pokeball
    def capturar_pokemon_sal(self):
        a= (((3*self.psmax)-2*self.psactual)*self.Rc*self.Rb)/(3*self.psmax)
        return a
    def aprendizaje_de_movimientos():
        pass

    def bonificacion_monetaria():
        pass
    

