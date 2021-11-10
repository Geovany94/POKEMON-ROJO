
class Tienda_poke:
    def __init__(self,dinero,a,b,c,d,e,f,g):
        self.dinero= dinero
        self.pocion= a
        self.superpocion=b
        self.hiperpocion=c
        self.pokeball=d
        self.superball=e
        self.ultraball=f
        self.masterball=g
        self.restaurar_todo= a,b,c

    def puntos_de_vida(self,opcion):
        
        if opcion == 1:
            self.pocion = self.pocion + 20
            self.dinero = self.dinero - 300
            if self.dinero <200:
                raise Exception('¡Error->MONEDAS INSUFICIES PARA HACER COMPRAS! ')
    def obejtos_captura(self):
        pass

