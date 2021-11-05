import os
import requests
from equipo import Equipo
from random import randint
#from TIENDA import tienda

equipo = Equipo(5)


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
        print('\t 5. prueba de clases')
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

        elif res == '5':
            print('Clase equipo')
            print(equipo)
            input('pause...')

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
    tipo_pokemon = pokemon['types']
    print("\n")
    print("\t Este es tu pokemon:")
    id = pokemon['id']
    print(f"\tNo. {pokemon['id']}")
    nombre = pokemon['name']
    print(f"\ttu pokemon: {pokemon['name']}")
    apo = apodo
    print(f"\tEl nombre que le diste es: {apodo}")
    nivel = 5
    print(f"\tSu nivel es: {nivel}")
    xp = 1500
    print(f"\tXp es :{xp}")
    print("\tTipo de Pokemon:")
    tipos = []
    for i, tipo in enumerate(tipo_pokemon):
        traduccion= requests.get(tipo['type']['url']).json()
        traducido=traduccion['names']
        tipo = print(f"\t{i+1}-  {traducido[4]['name']}")
        tipos.append(tipo)

    # Movimientos Muestra todo, tiene que ser solo cuatro
    print("\tMovimientos de Pokemon:")
    movi_pokemon = pokemon['moves']

    movimi = []
    for i, movimientos in enumerate(movi_pokemon):
        movimientos = print(f"\t{i+1} - {movi_pokemon[i]['move']['name']}")
        movimi.append(movimientos)


    print('\tStats del pokemon')
    statss = []
    for item in pokemon['stats']:
        print(f"\t- {item['stat']['name']}")
        stats = print(f"\t- {item['base_stat']} ")
        statss.append(stats)

    input('\tPresione una tecla para continuar')
    equipo.equipo_poke(id, nombre, apo, xp, tipos, movimi, statss)

 


def generar_pokemon():
    numero = randint(0, 75)
    
    clear()
    respuesta = requests.get('https://pokeapi.co/api/v2/type').json()
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
    especie = requests.get(pokemon['species']['url']).json()
    tipo_pokemon= pokemon['types']

    id = pokemon['id']

    nombre = pokemon['name']
    nivel = 5
    xp = 1500
    for i, tipo in enumerate(tipo_pokemon):
        traduccion= requests.get(tipo['type']['url']).json()
        traducido=traduccion['names']
        tipo = (f"{i+1}{traducido[4]['name']}")

    movimientos = print('\tTiene "danza dragon"') #----------------------------------------------------------- Componer -------------------------------
    
    for item in pokemon['stats']:
    
        nombre_stats= f"{item['stat']['name']}"
        stats = (f"{item['base_stat']}") 


    input('\tPresione una tecla para continuar')
    equipo.generar_poke_rival(id, nombre, xp, tipo, movimientos, nombre_stats, stats)
    

os.system('cls')
os.system('color F0')



print('\n\n\t\t By ANA ELENA CAMAJÁ RODRÍGUEZ               1590219')
print('\t\t By Cesar Geovany Ambrocio Quiej             1641417')
print('\t\t By Angel André Cotco Cuzal                  1518321')
print('\t\t By Dennys Rolando Yosimar Carreto Aguilon    2276616\n')


os.system('pause')
menu_inicial()
print('\t¡FIN PROGRAMA, GRACIAS POR PARTICIPAR ;)  !\n\n\n')
os.system('pause')
