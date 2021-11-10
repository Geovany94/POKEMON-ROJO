import sys
import time
import numpy as np 
import requests
from random import randint
from Generar_datos import Datos



# esta funcion me verifica si la lista que le mande esta vacia, valor=booleano(True,False)
def lista(lista):
    return not lista
    

def pokeapy(opcion, busca):
    pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
    return str(pokemon[busca]).capitalize()

def puntos_salud(self, opcion):
    pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
    salud= pokemon['stats'][0]['base_stat']
    vi= randint(0,int(salud))
    ps= Datos(self.nivel, salud, vi)
    ps_poke= ps.puntos_salud()
    return ps_poke

def movimientos(opcion):
    #EXTRAER INFORMACION DE LA POKEAPI
    movimientos=[]
    archivos=[]
    repetidos=[]
    pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
    poke=pokemon['moves']

#AGREGAR 4 NUMEROS ALEATORIOS PARA PODER OBTENER MOVIMIENTOS DE POKEMON
    if len(poke)>4:
        for i in range(0,4):
            asignar= randint(0,len(poke))
            movimientos.append(asignar)
    else:
        for i in range(len(poke)):
            movimientos.append(i)

#ENCONTRAR SI DENTRO DEL AREGLO EXISTEN VALORES REPETIDOS
    for i in movimientos:
        if i not in archivos:
            archivos.append(i)
        else:
            repetidos.append(i)

#ELIMINAR ELEMENTO REPETIDO
    if lista(repetidos)==True:
        pass
    else:
        eliminar= movimientos.index(repetidos[0])
        movimientos.pop(eliminar)
        movimientos.append(randint(0,len(poke)))
#TRADUCIR EL NOMBRE DEL MOVIMIENTO
    for i in range(0,len(movimientos)):
        m=movimientos[i]
        traduccion= requests.get(poke[m]['move']['url']).json()
        traducido=traduccion['names']
        print(f"  {traducido[5]['name']}")


def datos_combate(opcion):
    datos = []
    pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
    tipo_pokemon= pokemon['stats']
    for i, tipo in enumerate(tipo_pokemon):
        traduccion= requests.get(tipo['stat']['url']).json()
        traducido=traduccion['names']
        valor=tipo['base_stat']
        datos.append(valor)

   
# IMPRESION DE PALABRAS LETRA POR LETRA
def impresion_letras(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class  Pokemon : 
    def  __init__ ( self, opcion ,nivel, movi, señal='======='):
        self.opcion = opcion
        self.nivel= nivel 
        self.nombre=''
        self.movimiento= movi
        self.ps= 0
        self.escribir= señal
        


    def batalla(self, Pokemon2):

        #LUCHA DE DOS POKEMONS
        #IMPRIME INFORMACION DE LA PELEA
        self.ps= puntos_salud(self,self.opcion)
        self.nombre= pokeapy(self.opcion,'name' )
        print("-----BATALLA POKEMON-----")
        print(f"\n{self.nombre}")
        print("Nivel/", self.nivel)
        print("PS",self.escribir, self.ps)
      
        print("\nVS")
        

        #INFORMACION DEL POKEMON SALVAHE
        Pokemon2.ps= puntos_salud(self,Pokemon2.opcion)
        Pokemon2.nombre= pokeapy(Pokemon2.opcion,'name' )
        print(f"\n{Pokemon2.nombre}")
        print("Nivel/", Pokemon2.nivel)
        print("PS",Pokemon2.escribir, Pokemon2.ps)

        
    
        time.sleep(2)

       