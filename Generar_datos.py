

from lista import Mochila

mochila = Mochila()


class Datos:
    def __init__(self, nivel, ps, psindividual):
        self.vi = psindividual
        self.eb = ps
        self.n = nivel
        self.a= None
        
    
    def puntos_salud(self):
        lineal= (self.vi + 2 *self.eb)*(self.n/100) + 10 +self.n
        return lineal
        
    def datos_combate(self):
        datos_com= (self.vi + 2 *self.eb)*(self.n/100) + 5
        return datos_com

    def daños_punto_salud():
        pass

class Huir:
    def __init__(self, velocidadpoke, velocidadpokesal):
        self.A = velocidadpoke
        self.B = velocidadpokesal
        
    def huir_del_combate(self):
        f=(((self.A+128)/self.B)+30)% 256
        return f


class Capturar_poke:
    def __init__(self, ps, psactual, proporcion_captura, pokeball):
        self.psmax= ps
        self.psactual= psactual
        self.Rc= proporcion_captura
        self.Rb= pokeball
    def capturar_pokemon_sal(self):
        a= (((3*self.psmax)-2*self.psactual)*self.Rc*self.Rb)/(3*self.psmax)
        return a
    def aprendizaje_de_movimientos():
        pass

    def bonificacion_monetaria():
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
