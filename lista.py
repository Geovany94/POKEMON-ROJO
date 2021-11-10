from nodo import Nodo

class Mochila:

    def __init__(self):
        self.frente = None
        self.fondo = None
        self.tamanio = 0
        self.tam = 0
        


    def insertar_inicio(self, nivel, id, nombre, apodo, xp, tipo, movimiento, stat):
        self.tam += 1
        nuevo = Nodo( nivel, id, nombre, apodo, xp, tipo, movimiento, stat)
        #if self.tamanio < 6:
        if self.esta_vacia():
            self.frente = nuevo
            self.fondo = nuevo
        else:
            aux = self.frente
            self.frente = nuevo
            nuevo.siguiente = aux

            self.tamanio = self.tamanio + 1
        #else:
        #    self.eliminar_inicio()
        #    print('Ya alcanzo el numero maximo de Pokemon Equipo')
        #    input('presione una tecla para continuar')
            



    def menu(self):
        pass 

    def esta_vacia(self):
        return self.frente == None and self.fondo == None

    def recorrer(self):
        resultado = ''
        aux = self.frente
        while aux != None:
            if aux == self.fondo:
                resultado += str(aux)
            else:
                resultado += str(aux) + ' -> '
            aux = aux.siguiente
    
        return resultado

    def eliminar_inicio(self):
        if self.esta_vacia() == True:
            raise Exception('Subdesbordamiento de lista')

        elif self.frente == self.fondo:
            aux = self.frente
            self.frente = None
            self.fondo = None
            self.tamanio -= 1
            return aux

        else:
            aux = self.frente
            self.frente = self.frente.siguiente
            aux.siguiente = None
            self.tamanio -= 1
            return aux

    def __str__(self):
        resultado = 'Estado de la cola:\n'
        resultado += f"Tamaño: {self.tamanio}\n"
        resultado += f"Frente: {self.frente}\n"
        resultado += f"Fondo: {self.fondo}\n"
        return resultado