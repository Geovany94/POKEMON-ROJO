class Nodo:
    def __init__(self, nombre, carnet, monto, tiempo):

        self.nombre = nombre
        self.carnet = carnet
        self.monto = monto
        self.tiempo = tiempo
        self.siguiente = None

    def __str__(self):
        return (f'------------------------------------\n {self.nombre} \n carnet {self.carnet} \n-> Monto de transacción= Q {self.monto} \n-> {self.tiempo} ')
     

class Cola:
    def __init__(self, max = - 1):
        self.tamaño = 0
        self.frente = None
        self.final = None
        self.max = max 
        self.fuera= 0
        self.total= 0
        if self.max==-1:
            self.max= 'No hay limite de capacidad'


    def insertar (self, nombre, carnet, monto, fecha):
        
        nuevo= Nodo(nombre, carnet, monto, fecha)
        if self.frente == None and self.final == None:
            self.frente = nuevo
            self.final = nuevo
        elif self.tamaño == self.max:
            raise Exception('¡Error-> Desbordamiento de cola.! ')
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamaño += 1


    def recorrer(self):
        
        resultado = ''
        aux = self.frente
        while aux != None:
            resultado = resultado + str(aux) + '\n'
            aux = aux.siguiente
        return resultado


    def eliminar(self):
        # 1 - Crear el auxiliar (Señalar al frente)
        self.total = self.total+ int(self.frente.monto)
        aux = self.frente
        if self.tamaño == 0:
            raise Exception('Error: Subdesbordamiento de cola')
        if self.tamaño == 1:
            self.frente = None
            self.final = None
        else:
         # 2 - Mover el fente a siguiente elemeto
            self.frente = aux.siguiente 
         # 3 - QUitar enlaces
            aux.siguiente = None
        # 4 - Dsminuir tamaño
            self.tamaño =self.tamaño- 1
        # 5 - Devolver el nodo eliminado
        self.fuera =self.fuera +1
    
        return aux


    def atendidos(self):
        return f"Estudiantes atendidos: {str(self.fuera)}  \n Monto total transacciones:  Q {str(self.total)} \n Estudiantes en cola: {self.tamaño} "


    def maximo(self,num):
        self.max= num
        ingresados = int(self.tamaño)
        max= num
        if ingresados > max:
            res= ingresados- max
            for i in range(0,res):
                aux = self.frente
                if self.tamaño == 0:
                    raise Exception('Error: Subdesbordamiento de cola')
                if self.tamaño == 1:
                    self.frente = None
                    self.final = None
                else:
                    self.frente = aux.siguiente 
                    aux.siguiente = None
                self.tamaño = self.tamaño - 1


    def __str__(self):
        return f" En cola: {self.tamaño}\n Capacidad: {self.max}\n"