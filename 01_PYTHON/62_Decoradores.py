'''DECORADORES DE FUNCIONES Y USO'''

''' SI QUERMOS OBTENER EL NOMBRE DE LA FUNCION A LA CUAL SE HACE REFERENCIA Y LA DOCUMENTACION DE LA FUNCION
    QUE NO ES MAS QUE UN COMENTARIO QUE COLOQUEMOS DENTRO DE LA FUNCION, ANTES DE LA FUNCION ENVOLVENTE TENEMOS
    QUE COLOCAR @functools.wraps(func) Y ASI PODREMOS USAR LOS ATRIBUTOS __name__  Y __doc__
    

'''

import functools                        #! Hay que importarlo para que funcione la recuperacion del nombre de la funcion y comentario dentro de la funcion.


def mi_decorador(funcion):              #? PASO 3: Creamos una funcion con el nombre del decorador, que recibira la funcion del paso 1 como parametro
    @functools.wraps(funcion)
    def envolvente():                   #? PASO 4: Creamos una funcion envolvente , que incluira los pasos antes y despues de la funcion del paso 1
        print("Colocamos antes de ejecutar la funcion")   #? PASO 5: Ejecucion de pasos antes de nuestra funcion
        funcion()                                         #? funcion representa funcion_a_decorar()
        print("Ahora imprimimos algo despues de la funcion decorada")  #? PASO 6 : Pasos despues de ejecutr nuestra funcion
    return envolvente           #? PASO 7: Ojo, El return pertenece a la funcion mi_decorador()


@mi_decorador                           #? paso 2: Le añadimos un decorador con el nombre que queramos
def funcion_a_decorar():                #? PASO 1: Definimos una funcion 
    """ ESTA ES MI PRIMERA FUNCION DECORADORA Y __doc__ toma este comentario"""
    print("Funcion a decorar")
    
    
    
funcion_a_decorar()                     #! Ejecutamos la funcion y realmente llama a la funcion mi_decorador()
print(f"El nombre de la funcion es : {funcion_a_decorar.__name__}")
print(f"Sus comentarios internos son: {funcion_a_decorar.__doc__}\n")

'''FUNCION DECORADOR  CON ARGUMENTOS'''

def otro_decorador(func):
    @functools.wraps(func)
    def envolvente(*args, **kwargs):
        print(f"Llamando a {func.__name__} con argumentos: {args}, {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} retornó: {resultado}")
        return resultado
    return envolvente

@otro_decorador
def sumar(a, b):
    """SUMA 2 NUMEROS """
    """2DA LINEA DE COMENTARIOS"""        #! __doc__ solo toma el primer comentario....es decir, la linea anterior a esta. Si toma si es multilinea.
    return a + b

resultado_suma = sumar(5, 3)
print(f"El resultado de la suma es: {resultado_suma}")
print(f"El nombre de la funcion es : {sumar.__name__}")
print(f"Sus comentarios internos son: {sumar.__doc__}\n")



'''DECORADORES CON ARGUMENTOS PROPIOS'''
def decorador_con_argumentos(mensaje):              #? PASO 3: Creamos la funcion decoradora, que recibe el argumento,  que necesita crear el decorador real dentro de ella
    def decorador_real(func):                       #? PASO4: funcion decoradora real. Invoca la funcion bajo el nombre del decorador
        @functools.wraps(func)
        def envolvente(*args, **kwargs):            #? PASO 5: La funcion envolvente recibe los parametros que se inyectaran a la funcion Saludar
            print(f"Mensaje del decorador: {mensaje}")  #? PASO 6: Añadimos que se ejecuta antes de nuestra funcion. En este caso Muestra el parametro recibido 
            return func(*args, **kwargs)            #? PASO 7: Realmente ejecuta nuestra funcion saludar: inyecta los parametros a la funcion Saludar
        return envolvente                           #? PASO 8:El retorno en la misma funcion envolvente
    return decorador_real                           #? PASO 9:Aqui retorna la funcion decorador_real

@decorador_con_argumentos("¡Función ejecutada!")    #? PASO 2: Le añadimos el decorador con argumento
def saludar(nombre):                                #? PASO 1: Creamos nuestra funcion
    """SALUDA A UNA PERSONA"""
    print(f"¡Hola, {nombre}!")         

saludar("Ana")
print(f"El nombre de la funcion es : {saludar.__name__}")
print(f"Sus comentarios internos son: {saludar.__doc__}\n")

'''MULTIPLES DECORADORES'''

def decorador_mayusculas(func):             #? PASO 4: Tomara la funcion que tiene el decorador ( obtener_mensaje) 
    @functools.wraps(func)
    def envolvente(*args, **kwargs):        #? PASO 5: al colocar "*args, **kwargs" se pasaran los parametros ( cualquier cantidad a la funcion). Sino se pasan parametros no da error.
        resultado = func(*args, **kwargs)   #? PASO 6: Pasa los parametros a la funcion obtener_mensaje() , que al no tener no pasa le pasa nada. Guarda el resultado 
        return resultado.upper()            #? PASO 7: Convierte en mayuscula el string en resultado, que es "ESTE ES UN MENSAJE"
    return envolvente                       #? PASO 8: Retrorna la envolvente

def decorador_envolver_p(func):             #? PASO 9: Recibe la funcion que realmente viene de decorar_mayuscula
    @functools.wraps(func)
    def envolvente(*args, **kwargs):        #? PASO 10: Creamos la funcion envolvente y le colocamos parametros generales.
        resultado = func(*args, **kwargs)   #? PASO 11: Corremos nuestra funcion, donde los parametros, al no tener nada es como dejar la funcion sin parametros. Pero recibe el texto en mayuscula.
        return f"<p>{resultado}</p>"        #? PASO 12: Tomamos el texto en mayuscula y lo envolvemos en etiquetas de parrafo
    return envolvente                       #? PASO 13: retornamos la envolvente que a su vez retorna <p> ESTE ES UN MENSAJE</p>

@decorador_envolver_p               #? PASO 3: Segundo, se aplica envolver el texto con etiquetas de parrafo.
@decorador_mayusculas               #? PASO 2: Primero se aplica el decorador mas cercano -> convertir el texto a mayuscula
def obtener_mensaje():              #? PASO 1: Creamos nuestra funcion, obtener_mensaje. ( Que sera colocar un mensaje en minuscula)
    """CONVIERTE UN MENSAJE EN <p> MAYUSCULA </p>"""
    return "este es un mensaje"  

print(obtener_mensaje())
print(f"El nombre de la funcion es : {obtener_mensaje.__name__}")
print(f"Sus comentarios internos son: {obtener_mensaje.__doc__}\n")
