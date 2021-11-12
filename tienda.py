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
    # Funciones de uso
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
                curar = 20
                return curar 
            elif opcion == 2:
                self.superpocion -= 1
                curar = 50
                return curar
            elif opcion == 3:
                self.hiperpocion -= 1
                curar = 200
                return curar 
            elif opcion == 4:
                self.res_todo -= 1
                # se cura toda la vida, aun hay que ver esta parte!
                curar = 0
                return curar 
        else:
            print('No se puede usar este objeto, No tiene en existencias')

    # Funciones de compra
    def pokeballs(self, opcion):
        if opcion == 1:
            if self.dinero >= 200:
                self.pokeball += 1
                self.dinero = self.dinero - 200
                print('*Ha comprado una Pokeball*')
                print('Su nuevo saldo es: ',self.dinero)
                print('Total de pokeballs: ',self.pokeball)
            else:
                print('Dinero insuficiente')
            # os.system('pause')
            
        elif opcion == 2:
            if self.dinero >= 600:
                self.superball += 1
                self.dinero = self.dinero - 600
                print('*Ha comprado una Superball*')
                print('Su nuevo saldo es: ',self.dinero)
                print('Total de Superball: ',self.superball)
            else:
                print('Dinero insuficiente')
            # os.system('pause')
        
        elif opcion == 3:
            if self.dinero >= 1200:
                self.ultraball += 1
                self.dinero = self.dinero - 1200
                print('*Ha comprado una Ultraball*')
                print('Su nuevo saldo es: ',self.dinero)
                print('Total de Ultraball: ',self.ultraball)
            else:
                print('Dinero insuficiente')
            # os.system('pause')
        elif opcion == 4:
            if self.dinero >= 100000:
                self.masterball += 1
                self.dinero = self.dinero - 100000
                print('*Ha comprado una Masterball*')
                print('Su nuevo saldo es: ',self.dinero)
                print('Total de masterball: ',self.masterball)
            else:
                print('Dinero insuficiente')
            # os.system('pause')
    
    def obj_curativos(self,opcion):
        if opcion == 1:
            if self.dinero >= 300:
                self.pocion += 1
                self.dinero = self.dinero - 300
                print('*Ha comprado una Pocion*')
                print('Su nuevo saldo es: ',self.dinero)
                print('Total de Pocion: ',self.pocion)
            else:
                print('Dinero insuficiente')
            # os.system('pause')
        elif opcion == 2:
            if self.dinero >= 700:
                self.superpocion += 1
                self.dinero = self.dinero - 700
                print('*Ha comprado una Superpocion*')
                print('Su nuevo saldo es: ',self.dinero)
                print('Total de Superpocion: ',self.superpocion)
            else:
                print('Dinero insuficiente')
            # os.system('pause')
        elif opcion == 3:
            if self.dinero >= 1200:
                self.hiperpocion += 1
                self.dinero = self.dinero - 1200
                print('*Ha comprado una Hiperpocion*')
                print('Su nuevo saldo es: ',self.dinero)
                print('Total de Hiperpocion: ',self.hiperpocion)
            else:
                print('Dinero insuficiente')
            # os.system('pause')
        elif opcion == 4:
            if self.dinero >= 3000:
                self.res_todo += 1
                self.dinero = self.dinero - 3000
                print('*Ha comprado Restaurar vida completa*')
                print('Su nuevo saldo es: ',self.dinero)
                print('Total de Restaurar vida completa: ',self.res_todo)
            else:
                print('Dinero insuficiente')
            # os.system('pause')

    def ver_mochila(self):
        print('\tInventario de objetos')
        print('\tPoke ball')
        print('\t* Pokeball ',self.pokeball)
        print('\t* Superball ',self.superball)
        print('\t* Ultraball ',self.ultraball)
        print('\t* Masterball ',self.masterball)
        print('\tPociones ')
        print('\t* Pocion ',self.pocion)
        print('\t* Superpocion ',self.superpocion)
        print('\t* Hiperpocion ',self.hiperpocion)
        print('\t* Restaurar toda la vida ',self.res_todo)