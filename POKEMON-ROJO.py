import os
import requests
from equipo import Equipo
#from TIENDA import tienda
lista_equipo = Equipo()

print("Hola")
 

clear = lambda: os.system('cls')#limpiar pantalla usar siempre con libreria os 

def menu_inicial():
    os.system('cls')
    os.system('color E0')
    
    print('\n\t\tBIENVENIDO A POKEMON ROJO \n')
    print('\t Ingrese su nombre de entrenador Pokemon')
    entrenador= input('\t ')
    
    print('\t Pokemon inicial-- Pokemons disponibles:')
    print('\t 1->Bulbasaur')
    print('\t 2->Charmander')
    print('\t 3->Squirtle')
    res = str(input('\t ->'))
    if res=='1':
        acceder=1
        mote = input('\tIngrese mote para su pokemon: ')
        menu_principal(acceder, mote)
        

    elif res=='2':
        acceder=4
        mote = input('\tIngrese mote para su pokemon: ')
        menu_principal(acceder, mote)
    elif res=='3':
        acceder=7
        mote = input('\tIngrese mote para su pokemon: ')
        menu_principal(acceder, mote)
    else:
        print('\tERROR-> La opción elejida no existe.\n')
        os.system('pause')
        menu_inicial()
    
    


def menu_principal(opcion, mote):
    while True:
        os.system('color E0')
        os.system('cls')
        res=""
        pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
        pokemon_inicial= pokemon['name']
        print('\n\t\tMENÚ PRINCIPAL')
        print('_________________________________________________________')
        print('\t 1. Equipo Pokemon')
        print('\t 2. Batallas con Pokemons salvajes')
        print('\t 3. Pokédex')
        print('\t 4. Tienda')
        print('\t 0. Salir del juego')
        print('\n\tOPCION: "\t')
        res = str(input('\t '))
        if res=='1':
            equipo_pokemon(opcion, mote)
        elif res=='2':
            batalla_pokemon()
        elif res=='3':
            pokedex()
        elif res=='4':
            tienda()
        elif res=='0':
            break
        else:
            print('\tERROR-> La opción elejida no existe.\n')
            os.system('pause')
            

def batalla_pokemon():
    dinero=0
    pocion=0
    superpocion=0
    hiperpocion=0
    pokeball=0
    superball=0
    ultraball=0
    masterball=0
    tienda(pocion,superpocion,hiperpocion,pokeball,superball,ultraball,masterball)
    tienda_objetos(dinero)
def pokedex():
    pass
def tienda_objetos(dinero):
    os.system('cls')
    valor=dinero
    print('\n\t\tTIENDA POKEMON \n')
    print('\t 1-> Comprar objetos curativos')
    print('\t 2-> Comprar Poké Ball')
    res = str(input('\t ->'))
    if res=='1':
        print('\t   NOMBRE           |PUNTOS DE SALUD   |VALOR')
        print('\t-----------------------------------------------_')
        print('\t 1 Poción           |20                |300')
        print('\t 2 Superpoción      |50                |700')
        print('\t 3 Hiperpoción      |200               |1200')
        print('\t 4 Restaurar todo   |Vida completa     |3000')
        opcion= int(input('\t->	'))
        os.system('pause')
    elif res=='2':
        print('\t   NOMBRE           |PROPORCION DE    |VALOR')
        print('\t                    |CAPTURA          |')
        print('\t -------------------------------------------------')
        print('\t 1 Pokéball         |1                |200')
        print('\t 2 Superball        |1.5              |600')
        print('\t 3 Ultraball        |2                |1200')
        print('\t 4 Masterball       |255              |100000')
        opcion= int(input('\t->	'))
        os.system('pause')
    else:
        print('\tERROR-> La opción elejida no existe.\n')
        os.system('pause')

def equipo_pokemon(numero, apodo):

    clear()
    respuesta = requests.get('https://pokeapi.co/api/v2/type').json()
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
    especie = requests.get(pokemon['species']['url']).json()
    tipo_pokemon= pokemon['types']
    print("\n")
    print("\t Este es tu pokemon:")
    id = print(f"\tNo. {pokemon['id']}")
    nombre = print(f"\t{pokemon['name']}")
    apo = print(f"Su apodo de Pokemon es: {apodo}")
    nivel = print(f"\t 5")
    experiencia = print(f"\t1500")
    print("Tipo de Pokemon:")
    for i, tipo in enumerate(tipo_pokemon):
        traduccion= requests.get(tipo['type']['url']).json()
        traducido=traduccion['names']
        print(f"{i+1}-  {traducido[4]['name']}")
    print("\n\n")
    
    
    print('\tStats del pokemon')
    for item in pokemon['stats']:
        print('\tStats base')
        print(f"\t- {item['stat']['name']}")
        print(f"\t- {item['base_stat']} ")

    input('\tPresione una tecla para continuar')

    print("\tEste es tu pokemon:")
    id = print(f"\tNo. {pokemon['id']}")
    nombre = print(f"\ttu pokemon: {pokemon['name']}")
    apo = print(f"\tEl nombre que le diste es {apodo}")
    nivel = print(f"\tSu nivel es 5")
    experiencia = 1500






os.system('cls')
os.system('color F0')



print('\n\n\t\t By ANA ELENA CAMAJÁ RODRÍGUEZ               1590219')
print('\t\t By Cesar Geovany Ambrocio Quiej             1641417')
print('\t\t By Angel André Cotco Cuzal                  1518321')
print('\t\t By Denys Rolando Yosimar Carreto Aguilon    2276616\n')


print('\n\n\t\t By ANA ELENA CAMAJÁ RODRÍGUEZ   1590219\n')
print('\n\n\t\t By Cesar Geovany Ambrocio Quiej   1641417\n')
print('\n\n\t\t By Angel André Cotco Cuzal        1518321\n')
print('\n\n\t\t By Angel André Cotco Cuzal 1641417\n')
print('\n\n\t\t By Denys carreto \n')
print('\n\n\t\t By ELena \n')
print('\n\n\t\t By ELena \n')





os.system('pause')
menu_inicial()
print('\t¡FIN PROGRAMA, GRACIAS POR PARTICIPAR ;)  !\n\n\n')
os.system('pause')
