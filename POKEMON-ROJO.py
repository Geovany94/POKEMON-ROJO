import os
import requests
from equipo import Equipo
from random import randint
from lista import Mochila
from tienda import Tienda
from pokedex import pokedex_h
from Batalla_pokemon import Pokemon
equipo = Equipo(5)
mochila = Mochila()

tienda = Tienda(1000000)
po = Pokemon(0,0,0)
poke = pokedex_h()
tienda = Tienda(1000)
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
        movi_poke = movimientos_poke_inicial(acceder)
        equipo_pokemon(acceder, mote)
        menu_principal(acceder, mote, entrenador, movi_poke)
    elif res=='2':
        acceder=4
        mote = input('\tIngrese mote para su pokemon: ')
        equipo_pokemon(acceder, mote)
        movi_poke = movimientos_poke_inicial(acceder)
        menu_principal(acceder, mote, entrenador, movi_poke)
    elif res=='3':
        acceder=7
        mote = input('\tIngrese mote para su pokemon: ')
        equipo_pokemon(acceder, mote)
        movi_poke = movimientos_poke_inicial(acceder)
        menu_principal(acceder, mote, entrenador, movi_poke)
    else:
        print('\tERROR-> La opción elejida no existe.\n')
        os.system('pause')
        menu_inicial()
    
        

    
def menu_principal(opcion, mote,entrenador, movi_poke):

    while True:
        os.system('color D0')
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
            n = mochila.recorrer()
            s = po.devolver() 
            print(s)
            print(n)    
            input('pause...')
        elif res=='2':
            os.system('color 0B')
        # ENVIAR INFORMACION DEL POKEMON INICIAL
            nivel=5
            pokemon_inicial= Pokemon(opcion, nivel, movi_poke)
        # CREAR INFORMACION DEL POKEMON SALVAJE
            opcion_sal= randint(1,898)
            nivel_sal=randint(0,4)
            pokemon_salvaje= Pokemon(opcion_sal, nivel_sal, None)
            pokemon_inicial.batalla(pokemon_salvaje)
            os.system('pause')


        elif res=='3':
            d = po.devolver_h()
            print(d)
            input('pause...') 
        elif res=='4':
            os.system('cls')
            print('\n\t\tTIENDA POKEMON \n')
            print('\t 1-> Ver Mochila')
            print('\t 2-> Comprar objetos curativos')
            print('\t 3-> Comprar Pokéball')
            print('\tEliga una opcion')
            opc = int(input())
            if opc == 1:
                os.system('cls')
                tienda.ver_mochila()
                os.system('pause')
            elif opc == 2:
                os.system('cls')

                print('\t ***OBJETOS DE CURACION***')
                print('\t Dinero Disponible: ', tienda.dinero)
                print('\t   NOMBRE           |PUNTOS DE SALUD   |VALOR')
                print('\t------------------------------------------------')
                print('\t 1 Poción           |20                |300')
                print('\t 2 Superpoción      |50                |700')
                print('\t 3 Hiperpoción      |200               |1200')
                print('\t 4 Restaurar todo   |Vida completa     |3000')
                print('\tEliga una opcion')
                opcion2 = int(input())
                if opcion2 == 1:
                    tienda.obj_curativos(opcion2)
                elif opcion2 == 2:
                    tienda.obj_curativos(opcion2)
                elif opcion2 == 3:
                    tienda.obj_curativos(opcion2)
                elif opcion2 == 4:
                    tienda.obj_curativos(opcion2)
                os.system('pause')
            elif opc == 3:
                os.system('cls')
                print('\t ***POKE BALL***')
                print('\t Dinero Disponible: ', tienda.dinero)
                print('\t   NOMBRE           |PROPORCION DE    |VALOR ')
                print('\t                    |CAPTURA          |')
                print('\t -------------------------------------------------')
                print('\t 1 Pokéball         |1                |200')
                print('\t 2 Superball        |1.5              |600')
                print('\t 3 Ultraball        |2                |1200')
                print('\t 4 Masterball       |255              |100000')
                print('\tEliga una opcion')
                opcion3 = int(input())
                if opcion3 == 1:
                    tienda.pokeballs(opcion3)
                elif opcion3 == 2:
                    tienda.pokeballs(opcion3)
                elif opcion3 == 3:
                    tienda.pokeballs(opcion3)
                elif opcion3 == 4:
                    tienda.pokeballs(opcion3)
                else:
                    print('\tERROR-> La opción elejida no existe.\n')
                os.system('pause')
            else:
                print('\tERROR-> La opción elejida no existe.\n')
                os.system('pause')

            os.system('color 0B')


        elif res == '5':
            equipo_pokemon(7,'juan')
            equipo_pokemon(42,'juassn')
            equipo_pokemon(2,'juaadasn')
            equipo_pokemon(25,'jdsaduan')
            equipo_pokemon(32,'jan')

        elif res == '6':
            equipo_pokemon(21,'patricio')



        elif res=='0':
            break
        else:
            print('\tERROR-> La opción elejida no existe.\n')
            os.system('pause')
            
def movimientos_poke_inicial(opcion):
    movimientos=[]
    movi=[]
    pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
    poke=pokemon['moves']
    #AGREGAR 4 NUMEROS ALEATORIOS PARA PODER OBTENER MOVIMIENTOS DE POKEMON
    for i in range(0,2):
        asignar= randint(0,len(poke))
        movimientos.append(asignar)
    for i in range(len(movimientos)):
        m=movimientos[i]
        traduccion= requests.get(poke[m]['move']['url']).json()
        traducido=traduccion['names']
        movi.append(traducido[5]['name'])
    return movi


def pokedex():
    pass

def equipo_pokemon(numero, apodo):
    if mochila.tam > 5:
        mochila .eliminar_inicio()
        print('No se pueden mas de 6 pokemons')
        input('presiones una tecla...')

    else:    
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

        #movimi = []
        #for d in range(4):
                        #- ------------------------------------------------- Movimietos
        #    for i, movimientos in enumerate(movi_pokemon):
        movimi = movimientos(numero)                
        #        a = randint(0,60)
        #        mov = movi_pokemon[a]['move']['name']
                        #movimientos = print(f"\t{i+1} - {movi_pokemon[a]['move']['name']}")
        #    movimi.append(mov)
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

def lista(lista):
    return not lista

def movimientos(opcion):
    #EXTRAER INFORMACION DE LA POKEAPI
    movimi = []
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
        for d in range(4):
            m = movimientos[i]
            traduccion= requests.get(poke[m]['move']['url']).json()
            traducido=traduccion['names']
            
            mov =  traducido[5]['name']
        movimi.append(mov)

    return movimi

            #print(f"  {traducido[5]['name']}")
    


os.system('cls')



print('\n\n\t\t By ANA ELENA CAMAJÁ RODRÍGUEZ               1590219')
print('\t\t By Cesar Geovany Ambrocio Quiej             1641417')
print('\t\t By Angel André Cotco Cuzal                  1518321')
print('\t\t By Dennys Rolando Yosimar Carreto Aguilon    2276616\n')





os.system('pause')
menu_inicial()
print('\t¡FIN PROGRAMA, GRACIAS POR PARTICIPAR ;)  !\n\n\n')
os.system('pause')
