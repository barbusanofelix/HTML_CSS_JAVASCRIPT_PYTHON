
'''
Practica de Clases en Python con personajes.

Referencia: Video https://www.youtube.com/watch?v=JVNirg9qs4M
'''

class Personaje:
        
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida
        
            
    def getnombre(self):
        return self.nombre    
    def getfuerza(self):
        return self.fuerza  
    def getinteligencia(self):
        return self.inteligencia  
    def getdefensa(self):
        return self.defensa  
    def getvida(self):
        return self.vida  
    
    def setnombre(self, nombre):
        self.nombre=nombre
    def setfuerza(self, fuerza):
        self.fuerza=fuerza
    def setinteligencia(self, inteligencia):
        self.inteligencia=inteligencia    
    def setdefensa(self, defensa):
        self.defensa=defensa
    def setvida(self, vida):
        self.vida=vida      
        
    def atributos(self):
        print("\n",self.nombre,":",sep="")    
        print(f"{'Fuerza':<20} :{self.fuerza}")
        print(f"{'Inteligencia':<20} :{self.inteligencia}")
        print(f"{'Defensa':<20} :{self.defensa}")
        print(f"{'Vida':<20} :{self.vida}")    
        
    def subir_nivel(self,fuerza, inteligencia, defensa):    
        self.fuerza=self.fuerza+fuerza
        self.inteligencia=self.inteligencia+inteligencia
        self.defensa=self.defensa+defensa
     
    def esta_vivo(self):
         return self.vida>0    # si esta vivo devuelve true

    def morir(self):
        self.vida=0
        print(self.nombre, " ha muerto")
        
    def lesion_causada(self, oponente):
        lesion= self.fuerza-oponente.defensa    # Mi Fuerza - Defensa del aoponente
        if lesion<=0:
            lesion=self.fuerza*0.25    # Mi Fuerza x 0.25
        return lesion
    
    def atacar(self, oponente):
        lesion_causada=self.lesion_causada(oponente)
        oponente.vida=oponente.vida-lesion_causada
        print(self.nombre, "ha realizado", lesion_causada, "puntos de lesion_causada a ", oponente.nombre, "y le queda vida de", self.vida)    
        if oponente.esta_vivo():
            print("La vida de", oponente.nombre, "es", oponente.vida)
        else:
            oponente.morir()
        
class Guerrero(Personaje):    # Se agrega atributo adicional, daño de espada 

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada=espada    # Lesion que causa la espada.
        
    def atributos(self):
        super().atributos()                                     # llama el metodo atributos() de la super clase Personaje
        print(f"{'Lesion por espada:':<20} :{self.espada}")   
        
    def tipo_espada(self):
        opcion=int(input("Elige tipo espada, (1) Acero Valyrio daño 8. (2) Matadragones daño 10 : "))
        if opcion==1:
            self.espada=8
        elif opcion==2:
            self.espada=10
        else:
            print("Numero incorrecto")      
            
    def lesion_causada(self, oponente):
        lesion=self.fuerza*self.espada-oponente.defensa
        if lesion<=0:
            lesion=self.fuerza*self.espada*0.25   # Toma un 25% de fuerza x espada
            
        return lesion    # Mi Fuerza*Espada - Defensa del aoponente  

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,libro):  # Agrega Libro
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro=libro
        
    def atributos(self):
        super().atributos()    
        print(f"{'Libro :':<20} :{self.libro}")
        
    def lesion_causada(self, oponente):
        lesion=self.inteligencia*self.libro-oponente.defensa    # Mi Fuerza*Espada - Defensa del aoponente   
        if lesion<= 0:
            lesion=self.inteligencia*self.libro*0.25    # Mi Fuerza*Espada - Defensa del aoponente   
        return lesion
    
    
def combate(jugador1,jugador2):
    print("\n Combate :", jugador1.nombre, "contra", jugador2.nombre,"\n")
    turno=0
    print("-"*100)
    while jugador1.esta_vivo() and jugador2.esta_vivo:
        turno+=1
        print("\n Turno", turno)
        print("Accion de ",jugador1.nombre, "con vida:",jugador1.vida)
        jugador1.atacar(jugador2)
        print("Accion de ",jugador2.nombre, "con vida:",jugador1.vida)
        jugador2.atacar(jugador1)
        print(f"{jugador1.nombre} esta vivo", jugador1.esta_vivo()) 
        print(f"{jugador2.nombre} esta vivo", jugador2.esta_vivo())
       
    if jugador1.esta_vivo():
        print("Ha ganado ", jugador1.nombre,"con vida:",jugador1.vida)
    elif jugador2.esta_vivo():
        print("Ha ganado ", jugador2.nombre,"con vida:",jugador2.vida)
    else:
        print("Empate, por muerte de ambos:", jugador1.nombre,"y",jugador2.nombre)
    print("="*100)                 
        
        
                    

goku=Personaje("Goku",20,15,50,100)
guts=Guerrero("Guts", 20,15,50,100,5)
vanessa=Mago("Vanessa", 20,15,50,100,5)
goku.esta_vivo()
combate(goku,guts)
goku.atributos()
guts.atributos()
vanessa.atributos()

goku.atacar(guts)
guts.atacar(vanessa)
vanessa.atacar(goku)

goku.atributos()
guts.atributos()
vanessa.atributos()



