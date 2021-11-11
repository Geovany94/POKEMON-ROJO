
import os   #LIBRERIA QUE LIMPIA LA PANTALLA, DA COLOR O UNA PAUSA
import requests #LIBRERIA QUE PERMITE EL ENTORNO VIRTUAL
from random import randint #RAMDOM LA LIBRERIA RANDINT FUNCION PARA ENCONTRAR NUMERO ALEATORIO
from Batalla_pokemon import Pokemon, movimientos #CLASE





clear = lambda: os.system('cls')#limpiar pantalla usar siempre con libreria os 
os.system('cls')
os.system('color 0F')
print('\n\n\t\t By ANA ELENA CAMAJÁ RODRÍGUEZ               1590219')
print('\t\t By Cesar Geovany Ambrocio Quiej             1641417')
print('\t\t By Angel André Cotco Cuzal                  1518321')
print('\t\t By Denys Rolando Yosimar Carreto Aguilon    2276616\n')
os.system('pause')




def menu_principal(opcion, mote, entrenador, movi_poke):
    while True:
        os.system('color E0')
        os.system('cls')
        print('\n\t\tMENÚ PRINCIPAL')
        print('_________________________________________________________')
        print('\t 1. Equipo Pokemon')
        print('\t 2. Batallas con Pokemons salvajes')
        print('\t 3. Pokédex')
        print('\t 4. Tienda')
        print('\t 0. Salir del juego')
        print('\n\tOPCION: "\t')
        print(movi_poke)
        res = str(input('\t '))
        if res=='1':
            pass

    #ACA EMPIEZA EL MENÚ BATALLA CON POKEMONS SALVAJE 
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

            dinero=20
            pocion=0
            superpocion=0
            hiperpocion=0
            pokeball=1
            superball=0
            ultraball=0
            masterball=0
            compras= (dinero, pocion,
            superpocion, hiperpocion, pokeball,
            superball, ultraball,masterball)
        
        elif res=='3':
           pass
        elif res=='4':
            os.system('cls')
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
                po= int(input('\t->	'))
                compras.puntos_de_vida(po)
                os.system('pause')
            elif res=='2':
                print('\t   NOMBRE           |PROPORCION DE    |VALOR')
                print('\t                    |CAPTURA          |')
                print('\t -------------------------------------------------')
                print('\t 1 Pokéball         |1                |200')
                print('\t 2 Superball        |1.5              |600')
                print('\t 3 Ultraball        |2                |1200')
                print('\t 4 Masterball       |255              |100000')
                po= int(input('\t->	'))
                compras.obejtos_captura(po)
                os.system('pause')
            else:
                print('\tERROR-> La opción elejida no existe.\n')
                os.system('pause')
    
        elif res=='0':
            pass
        else:
            print('\tERROR-> La opción elejida no existe.\n')
        os.system('pause')

# MENU 1 EQUIPO POKEMON 
def equipo_pokemon(numero, apodo, entrenador):
    
    while True:
        print('\n\t\tINFORMACION EQUIPO POKEMON')   
        print('_________________________________________________________')
        print('\t 1. Datos Pokemons')
        print('\t 2. Datos de combate')
        print('\t 0. Salir')
        opc=str(input('\t'))

        if opc=='1':
            pass
    nivel = 5
    clear()
    respuesta = requests.get('https://pokeapi.co/api/v2/type').json()
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
    especie = requests.get(pokemon['species']['url']).json()
    tipo_pokemon= pokemon['types']
    print("\n")
    print("\t Este es tu pokemon:")
    id = print(f"\tNo. {pokemon['id']}")
    nombre = print(f"\ttu pokemon: {pokemon['name']}")
    apo = print(f"\tEl nombre que le diste es {apodo}")
    nive = print(f"\tSu nivel es {nivel}")
    experiencia = print(f"\t1500")
    print("\tTipo de Pokemon:")
    for i, tipo in enumerate(tipo_pokemon):
        traduccion= requests.get(tipo['type']['url']).json()
        traducido=traduccion['names']
        tipo = (f"{traducido[4]['name']}")
        print(f"\t{i+1}-  {traducido[4]['name']}")
    mov = 0
    
    print('\tStats del pokemon')
    for item in pokemon['stats']:
        print('')
        stats = (f"{item['base_stat']}") 
        print(f"\t- {item['stat']['name']}")
        print(f"\t- {item['base_stat']} ")

    input('\tPresione una tecla para continuar')

    equipo = Equipo(id, nombre, apo, nivel, experiencia, tipo, mov, stats)






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
    


while True:
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
        menu_principal(acceder, mote, entrenador, movi_poke)
    elif res=='2':
        acceder=4
        mote = input('\tIngrese mote para su pokemon: ')
        movi_poke = movimientos_poke_inicial(acceder)
        menu_principal(acceder, mote, entrenador, movi_poke)
    elif res=='3':
        acceder=7
        mote = input('\tIngrese mote para su pokemon: ')
        movi_poke = movimientos_poke_inicial(acceder)
        menu_principal(acceder, mote, entrenador, movi_poke)
    else:
        print('\tERROR-> La opción elejida no existe.\n')
        os.system('pause')
    
    
 
print('\t¡FIN PROGRAMA, GRACIAS POR PARTICIPAR ;)  !\n\n\n')
os.system('pause')
