import os
import requests
from equipo import Equipo
from random import randint
from lista import Mochila
from tienda import Tienda

equipo = Equipo(5)
mochila = Mochila()
tienda = Tienda(1000)

from pokedex import pokedex_h
#from TIENDA import tienda

equipo = Equipo(5)
mochila = Mochila()
poke = pokedex_h()



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

        equipo_pokemon(acceder, mote)
        
        menu_principal(acceder, mote, entrenador)


    elif res=='2':
        acceder=4
        mote = input('\tIngrese mote para su pokemon: ')
        equipo_pokemon(acceder, mote)
        menu_principal(acceder, mote, entrenador)
        
    elif res=='3':
        acceder=7
        mote = input('\tIngrese mote para su pokemon: ')
        equipo_pokemon(acceder, mote)
        menu_principal(acceder, mote,entrenador)

    else:
        print('\tERROR-> La opción elejida no existe.\n')
        os.system('pause')
        menu_inicial()
    
def menu_principal(opcion, mote,entrenador):

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

            
            clear()
            #print('\n\t\tBienvenido a tu equipo pokemon')
            #print(f"1. {equipo.apodo}")
            #equipo_pokemon(opcion, mote)
            #print(equipo)
            #
            
            n = mochila.recorrer()
            print(n)
            input('pause...')
            

            

        elif res=='2':
            batalla_pokemon()
        elif res=='3':
            pokedex()
        elif res=='4':
<<<<<<< Updated upstream
=======




            tienda()
                        


>>>>>>> Stashed changes
            os.system('cls')
            print('\n\t\tTIENDA POKEMON \n')
            print('\t 1-> Ver Mochila')
            print('\t 2-> Comprar objetos curativos')
            print('\t 3-> Comprar Pokéball')
            print('\tEliga una opcion')
            opc = int(input())
            if opc == 1:
                os.system('cls')
                print('\tInventario de objetos')
                print('\tPoke ball')
                print('\t* Pokeball ',tienda.pokeball)
                print('\t* Ultraball ',tienda.ultraball)
                print('\t* Superball ',tienda.superball)
                print('\t* Masterball ',tienda.masterball)
                print('\tPociones ')
                print('\t* Pocion ',tienda.pocion)
                print('\t* Super pocion ',tienda.superpocion)
                print('\t* Hiperpocion ',tienda.hiperpocion)
                print('\t* Restaurar toda la vida ',tienda.res_todo)
                os.system('pause')
            elif opc == 2:
                os.system('cls')
                print('\t ***OBJETOS DE CURACION***')
                print('\t   NOMBRE           |PUNTOS DE SALUD   |VALOR')
                print('\t Dinero Disponible: ', tienda.dinero)
                print('\t------------------------------------------------')
                print('\t 1 Poción           |20                |300')
                print('\t 2 Superpoción      |50                |700')
                print('\t 3 Hiperpoción      |200               |1200')
                print('\t 4 Restaurar todo   |Vida completa     |3000')
                print('\tEliga una opcion')
                opcion = int(input())
                if opcion == 1:
                    tienda.obj_curativos(opcion)
                elif opcion == 2:
                    tienda.obj_curativos(opcion)
                elif opcion == 3:
                    tienda.obj_curativos(opcion)
                elif opcion == 4:
                    tienda.obj_curativos(opcion)
                os.system('pause')
            elif opc == 3:
                os.system('cls')
                print('\t ***POKE BALL***')
                print('\t   NOMBRE           |PROPORCION DE    |VALOR ')
                print('\t                    |CAPTURA          |')
                print('\t Dinero Disponible: ', tienda.dinero)
                print('\t -------------------------------------------------')
                print('\t 1 Pokéball         |1                |200')
                print('\t 2 Superball        |1.5              |600')
                print('\t 3 Ultraball        |2                |1200')
                print('\t 4 Masterball       |255              |100000')
                print('\tEliga una opcion')
                opcion = int(input())
                if opcion == 1:
                    tienda.pokeballs(opcion)
                elif opcion == 2:
                    tienda.pokeballs(opcion)
                elif opcion == 3:
                    tienda.pokeballs(opcion)
                elif opcion == 4:
                    tienda.pokeballs(opcion)
                os.system('pause')
            else:
                print('\tERROR-> La opción elejida no existe.\n')
                os.system('pause')


        elif res == '5':
            generar_pokemon_h(12,'juan')
            generar_pokemon_h(21,'juaaasdn')
            generar_pokemon_h(32,'judsan')





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


def pokedex():
    pass

def equipo_pokemon(numero, apodo):
    
        
    nivel = 5

    clear()
    respuesta = requests.get('https://pokeapi.co/api/v2/type').json()
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
    especie = requests.get(pokemon['species']['url']).json()
    tipo_pokemon = pokemon['types']
    nivel = 5
            #print("\n")
            #print("\t Este es tu pokemon:")
    id = pokemon['id']
                #print(f"\tNo. {pokemon['id']}")
    nombre = pokemon['name']
                #print(f"\ttu pokemon: {pokemon['name']}")
    apo = apodo
                #print(f"\tEl nombre que le diste es: {apodo}")
                #nivel = 5
                #print(f"\tSu nivel es: {nivel}")
    xp = pokemon['base_experience']
                #print(f"\tXp es :{xp}")
                #print("\tTipo de Pokemon:")
    tipos = []
    for i, tipo in enumerate(tipo_pokemon):
        traduccion= requests.get(tipo['type']['url']).json()
        traducido=traduccion['names']
        tip = traducido[4]['name']
                    #tipo = print(f"\t{i+1}-  {traducido[4]['name']}")
        tipos.append(tip)

                # Movimientos Muestra todo, tiene que ser solo cuatro
    movi_pokemon = pokemon['moves']

    movimi = []
    for d in range(4):
                    
        for i, movimientos in enumerate(movi_pokemon):
                        
            a = randint(0,65)
            mov = movi_pokemon[a]['move']['name']
                    #movimientos = print(f"\t{i+1} - {movi_pokemon[a]['move']['name']}")
        movimi.append(mov)
                #print(f"\tSus movimientos son {movimi}")

                #print('\tStats del pokemon')
    statss = []
                
    for item in pokemon['stats']:
        item['stat']['name']
                        #stats = print(f"\t- {item['base_stat']} ")
        stat = item['base_stat']
        statss.append(stat)

                #input('\tPresione una tecla para continuar')
                #equipo.equipo_poke(id, nombre, apo, xp, tipos, movimi, statss)
    mochila.insertar_inicio(nivel, id, nombre, apodo, xp, tipos, movimi, statss)

    



def generar_pokemon_h(numero, x):
    atrapado = False
    if x == True:
        atrapado = True

    elif x == False:
        atrapado = False


    nivel = 5
    clear()
    respuesta = requests.get('https://pokeapi.co/api/v2/type').json()
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
    especie = requests.get(pokemon['species']['url']).json()
    tipo_pokemon = pokemon['types']
    nivel = 5
    #print("\n")
    #print("\t Este es tu pokemon:")
    id = pokemon['id']
        #print(f"\tNo. {pokemon['id']}")
    nombre = pokemon['name']
        #print(f"\ttu pokemon: {pokemon['name']}")
        #print(f"\tEl nombre que le diste es: {apodo}")
        #nivel = 5
        #print(f"\tSu nivel es: {nivel}")
    xp = pokemon['base_experience']
        #print(f"\tXp es :{xp}")
        #print("\tTipo de Pokemon:")
    tipos = []
    for i, tipo in enumerate(tipo_pokemon):
        traduccion= requests.get(tipo['type']['url']).json()
        traducido=traduccion['names']
        tip = traducido[4]['name']
            #tipo = print(f"\t{i+1}-  {traducido[4]['name']}")
        tipos.append(tip)

        # Movimientos Muestra todo, tiene que ser solo cuatro
    movi_pokemon = pokemon['moves']

    movimi = []
    for d in range(4):
            
        for i, movimientos in enumerate(movi_pokemon):
                
            a = randint(0,60)
            mov = movi_pokemon[a]['move']['name']
            #movimientos = print(f"\t{i+1} - {movi_pokemon[a]['move']['name']}")
        movimi.append(mov)
        #print(f"\tSus movimientos son {movimi}")

        #print('\tStats del pokemon')
    statss = []
        
    for item in pokemon['stats']:
        item['stat']['name']
                #stats = print(f"\t- {item['base_stat']} ")
        stat = item['base_stat']
        statss.append(stat)

        #input('\tPresione una tecla para continuar')
        #equipo.equipo_poke(id, nombre, apo, xp, tipos, movimi, statss)
    poke.insertar_inicio(nivel, id, nombre, xp, tipos, movimi, statss, atrapado)

    

def pokedex():
    print('Bienvedido a la pokedex')
    c = poke.recorrer()
    print(c)
    input('pause...')

    


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
