from nodo_poke import Nodo_poke

class pokedex_h:

    def __init__(self):
        self.frente = None
        self.fondo = None
        self.tamanio = 0
        

    def insertar_inicio(self, nivel, id, nombre, xp, tipo, movimiento, stat, atrapado):
       
        
        nuevo = Nodo_poke( nivel, id, nombre, xp, tipo, movimiento, stat, atrapado)
        if self.esta_vacia():
            self.frente = nuevo
            self.fondo = nuevo

        else:
            aux = self.frente
            self.frente = nuevo
            nuevo.siguiente = aux

            self.tamanio +=1

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


    def __str__(self):
        resultado = 'Estado de la cola:\n'
        resultado += f"Tamaño: {self.tamanio}\n"
        resultado += f"Frente: {self.frente}\n"
        resultado += f"Fondo: {self.fondo}\n"
        return resultado