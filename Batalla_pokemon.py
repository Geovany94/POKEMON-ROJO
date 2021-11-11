import sys
import time
import requests
from random import randint
from Generar_datos import Capturar_poke, Datos, Huir
from lista import Mochila


mochila = Mochila()


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
        print( traducido[5]['name'])


def datos_combate(opcion):
    datos=[]
    pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/").json()
    tipo_pokemon= pokemon['stats']
    for i, tipo in enumerate(tipo_pokemon):
        traduccion= requests.get(tipo['stat']['url']).json()
        traducido=traduccion['names']
        valor=tipo['base_stat']
        datos.append(valor)
    return str(datos)

   
# IMPRESION DE PALABRAS LETRA POR LETRA
def impresion_letras(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def equipo_pokemon(numero, apodo):
    if mochila.tam > 5:
        mochila .eliminar_inicio()
        print('No se pueden mas de 6 pokemons')
        input('presiones una tecla...')

    else:    
        nivel = 5

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
        

class  Pokemon : 
    def  __init__ ( self, opcion ,nivel, movi, señal='======='):
        self.opcion = opcion
        self.nivel= nivel 
        self.nombre=''
        self.movimiento= movi
        self.ps= 0
        self.escribir= señal
        self.estadisticas= []
        self.id= 0

    def devolver(self):
        return mochila.recorrer()
        


    def batalla(self, Pokemon2):

        #LUCHA DE DOS POKEMONS
        #IMPRIME INFORMACION DE LA PELE
        self.id= pokeapy(self.opcion,'id')
        self.ps= puntos_salud(self,self.opcion)
        self.estadisticas= datos_combate(self.opcion)
        self.nombre= pokeapy(self.opcion,'name' )
        print("-----BATALLA POKEMON-----")
        print(f"\n{self.nombre}")
        print("Nivel/", self.nivel)
        print("PS",self.escribir, self.ps)
      
        print("\nVS")

        #INFORMACION DEL POKEMON SALVAHE
        Pokemon2.id= pokeapy(Pokemon2.opcion, 'id')
        Pokemon2.ps= puntos_salud(self,Pokemon2.opcion)
        Pokemon2.estadisticas= datos_combate(Pokemon2.opcion)
        Pokemon2.nombre= pokeapy(Pokemon2.opcion,'name' )
        print(f"\n{Pokemon2.nombre}")
        print("Nivel/", Pokemon2.nivel)
        print("PS",Pokemon2.escribir, Pokemon2.ps)
        ps_pokeini=self.ps
        ps_pokesal=Pokemon2.ps


 
        while (self.ps > 0) and (Pokemon2.ps > 0):
            pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.opcion}").json()
            propor_captura= pokemon['capture_rate']

            print(self.id)
            print(f"\n{self.nombre}\t\tPS\t{self.ps}")
            print(Pokemon2.id)
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.ps}\n")

            print(f"Go {self.nombre}!")
            print('1. ATACAR')
            print('2. CAPTURAR')
            print('3. OBJETOS CURATIVOS')
            print('4. HUIR')
            print('5. HISTORIAL DE COMBATE')
            eleccion=int(input())
            if eleccion==1:
                time.sleep(1)
                print(f"\n{self.name}\t\tHLTH\t{self.health}")
                print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
                time.sleep(0.5)
                #if Pokemon2.ps <= 0:
                    #impresion_letras("\n..." + Pokemon2.name + 'FUE DERROTADO')
                   # break

            elif eleccion==2:
                a=0
                pokeball=1
                superball=1.5
                ultraball=2
                masterball=255
                print("1. Pokeball", pokeball)
                print("2. Superball", superball)
                print("3. Ultraball", ultraball)
                print("4. Masterball", masterball)
                opcion=int(input())
                if opcion ==1:
                    infor= Capturar_poke(ps_pokeini,self.ps,propor_captura, pokeball)
                    a= infor.capturar_pokemon_sal()
                    pokeball= pokeball-1
                elif opcion ==2:
                    infor= Capturar_poke(ps_pokeini,self.ps,propor_captura, superball)
                    a= infor.capturar_pokemon_sal()
                    superball= superball-1.5
                elif opcion ==3:
                    infor= Capturar_poke(ps_pokeini,self.ps,propor_captura, ultraball)
                    a= infor.capturar_pokemon_sal()
                    ultraball= ultraball-2
                elif opcion ==4:
                    infor= Capturar_poke(ps_pokeini,self.ps,propor_captura, masterball)
                    a= infor.capturar_pokemon_sal()
                    masterball= masterball-255
                else:
                    print('\tERROR-> La opción elejida no existe.\n')

                if a>=255:
                    impresion_letras("'¡POKEMON CAPTURADO!...")
                    mote = input('Ingrese un nombre para su pokemon: ')
                    equipo_pokemon(Pokemon2.id, mote)
                    Pokemon2.ps = 0
                    
                else:
                    impresion_letras("'¡POKEMON NO CAPTURADO!...")



# CODIGO DE LA SELECCION "OBJETOS CURATICOS"
            elif eleccion==3:
                pocion=20
                superpocion=50
                hiperpocion=200
                restaurart_todo= ps_pokeini
                print("1. Pocion", pocion)
                print("2. Superpocion", superpocion)
                print("3. Hiperpocion", hiperpocion)
                print("4. Restaurar todo", restaurart_todo)
                opcion=int(input())
                if opcion ==1:
                    pocion= pocion-20
                    self.ps= self.ps +20
                elif opcion ==2:
                    superpocion= superpocion-50
                    self.ps= self.ps +50
                elif opcion ==3:
                    hiperpocion= hiperpocion-200
                    self.ps= self.ps +200
                elif opcion ==4:
                    restaurart_todo= restaurart_todo-20
                    self.ps= ps_pokeini
                else:
                    print('\tERROR-> La opción elejida no existe.\n')

    # CODIGO DE LA SELECCION "HUIR DEL COMBATE"
            elif eleccion==4:
                pokemonini= requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.opcion}/").json()
                poke_velocidad= pokemonini['stats'][5]['base_stat']
                pokemonsal= requests.get(f"https://pokeapi.co/api/v2/pokemon/{Pokemon2.opcion}/").json()
                pokesal_velocidad= pokemonsal['stats'][5]['base_stat']
                infor= Huir(poke_velocidad,pokesal_velocidad)
                f= infor.huir_del_combate()
                aleatorio= randint(0,255)
                if aleatorio<f:
                    impresion_letras("¡HUIDA EXITOSA!...")
                else:
                    impresion_letras("¡NO SE PUEDE HUIR!...")
    # CODIGO DE LA SELECCION "HISTORIAL COMBATE"
            elif eleccion==5:
                print(10)
            else:
                print('\tERROR-> La opción elejida no existe.\n')

            
           

           # print(f"Go {Pokemon2.name}!")
    
            #time.sleep(1)
        
            #time.sleep(1)
            #print(f"{self.name}\t\tHLTH\t{self.health}")
            #print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            #time.sleep(.5)

            # Check to see if Pokemon fainted
            #if self.bars <= 0:
               # print("\n..." + self.name + ' fainted.')
               # break




        #pokemon1= Pokemon(self.name, self.nivel)
        #pokemonsal= Pokemon(Pokemon2.name, Pokemon2.nivel)
        #pokemon1.ps= self.ps
        #pokemonsal.ps= Pokemon2.ps
        #pokemon1.estadisticas= {self.estadisticas}
        #pokemonsal.estadisticas= {Pokemon2.estadisticas}
        #pokemon1.ataques = [Ataque()]
        time.sleep(2)
     