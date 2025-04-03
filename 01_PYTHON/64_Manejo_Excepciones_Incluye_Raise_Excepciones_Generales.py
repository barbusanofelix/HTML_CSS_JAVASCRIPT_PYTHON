''''MANEJO DE EXCEPCIONES EN PYTHON'''

# Definimos una funcion de dividir

def dividir(numerador,denominador):
    try:
        if denominador==0:     
            raise Exception("Denominador igual a cero, lanzada por mi")             #? Lanzar una Excepcion por nuestra parte 
        resultado=numerador/denominador
        print(f"La division de {numerador}/{denominador} es :{resultado}")
    except Exception as e:
        print(f"Ocurrio un error del tipo {e}")
        
    else:
        print("No ocurrio ningun error")                                            #? Este es opcional. Se ejecutara sino ocurrio un error y aqui podriamos incluir cualquier codigo si no huno error.
    finally:
        print("Finaly siempre se ejecuta, haya o no error: Se termino la revision\n")  
        
   
   
   
'''  SI QUEREMOS HACERLO POR TIPO DE ERROR PODRIAMOS CAMBIAR EL EXCEPT ANTERIOR POR ESTAS LINEAS
    except  ZeroDivisionError:                      # Aqui podemos cambiar para Exception pero te manda al mismo mensaje  si paso una letra.
        print(f"**ERROR DIVISION POR CERO**  : No puedes dividir entre cero, {numerador}/{denominador}")   
    except  TypeError:
        print(f"**ERROR NO PUEDES DIVIDIR STRINGS**  : No puedes usar letras o caracteres o strings , {numerador} entre {denominador}")
'''
dividir(20,10)
dividir(10,0)
dividir(10,'0')
dividir('/', 8)



