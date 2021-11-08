import os
class Tienda:
    def __init__(self,dinero):
        self.dinero = dinero
        self.pocion = 0
        self.superpocion = 0
        self.hiperpocion = 0
        self.res_todo = 0
        self.pokeball = 0
        self.superball = 0
        self.ultraball = 0
        self.masterball = 0
    
    def usar_pokeballs(self, opcion):
        if self.pokeball > 0 or self.superball > 0 or self.ultraball > 0 or self.masterball > 0:    
            if opcion == 1:
                self.pokeball -= 1
            elif opcion == 2:
                self.superball -= 1
            elif opcion == 3:
                self.ultraball -= 1
            elif opcion == 4:
                self.masterball -= 1
        else:
            print('No se puede usar este objeto, No tiene en existencias')
            
    def usar_pociones(self, opcion):
        if self.pocion > 0 or self.superpocion > 0 or self.hiperpocion > 0 or self.res_todo > 0:
            if opcion == 1:
                self.pocion -= 1
            elif opcion == 2:
                self.superpocion -= 1
            elif opcion == 3:
                self.hiperpocion -= 1
            elif opcion == 4:
                self.res_todo -= 1
        else:
            print('No se puede usar este objeto, No tiene en existencias')

    
    def puntos_de_vida(self,opcion):
        if opcion == 1:
            self.pocion = self.pocion + 20
            self.dinero = self.dinero - 300
            if self.dinero <200:
                raise Exception('¡Error->MONEDAS INSUFICIES PARA HACER COMPRAS! ')
    
    def pokeballs(self, opcion):
        if opcion == 1:
            if self.dinero >= 200:
                self.pokeball =+ 1
                self.dinero = self.dinero - 200
                print('*Ha comprado una Pokeball*')
            else:
                print('Dinero insuficiente')
            
        elif opcion == 2:
            if self.dinero >= 600:
                self.superball =+ 1
                self.dinero = self.dinero - 600
                print('*Ha comprado una Superball*')
            else:
                print('Dinero insuficiente')
        
        elif opcion == 3:
            if self.dinero >= 1200:
                self.ultraball =+ 1
                self.dinero = self.dinero - 1200
                print('*Ha comprado una Ultraball*')
            else:
                print('Dinero insuficiente')
        elif opcion == 4:
            if self.dinero >= 100000:
                self.masterball =+ 1
                self.dinero = self.dinero - 100000
                print('*Ha comprado una Masterball*')
            else:
                print('Dinero insuficiente')
    
    def obj_curativos(self,opcion):
        if opcion == 1:
            if self.dinero >= 300:
                self.pocion =+ 1
                self.dinero = self.dinero - 300
                print('*Ha comprado una Pocion*')
            else:
                print('Dinero insuficiente')
        elif opcion == 2:
            if self.dinero >= 700:
                self.superpocion =+ 1
                self.dinero = self.dinero - 700
                print('*Ha comprado una Superpocion*')
            else:
                print('Dinero insuficiente')
        elif opcion == 3:
            if self.dinero >= 1200:
                self.hiperpocion =+ 1
                self.dinero = self.dinero - 1200
                print('*Ha comprado una Hyperpocion*')
            else:
                print('Dinero insuficiente')
        elif opcion == 4:
            if self.dinero >= 3000:
                self.res_todo =+ 1
                self.dinero = self.dinero - 3000
                print('*Ha comprado Restaurar vida completa*')
            else:
                print('Dinero insuficiente')

    