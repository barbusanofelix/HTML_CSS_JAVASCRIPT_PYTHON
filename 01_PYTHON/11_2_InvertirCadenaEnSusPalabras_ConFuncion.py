def rev_sentence(sentence):
    words = sentence. split(' ')    # toma la cadena de entrada sentence y la divide en una lista de palabras, separando por ' '.
    '''
    reversed(words): Esta función toma la lista words y devuelve un iterador que recorre la lista en orden inverso.
    ' '.join(...): Este método toma el iterador devuelto por reversed(words) y une las palabras en una sola cadena.
    El separador utilizado para unir las palabras es un espacio en blanco (' ').
    El resultado es una nueva cadena llamada reverse_sentence, que contiene las palabras de la oración original en orden inverso.
    '''
    reverse_sentence = ' '.join(reversed(words))  #Aqui ya tenemos la oracion en orden inverso.
    return reverse_sentence                       # Devuelve la oracion en orden inverso

# AQUI EL CORAZON DEL PROGRAMA PRINCIPAL.
if __name__ == "__main__":
    entrada = 'geeks quiz practice code'
    print (rev_sentence(entrada))


'''
El bloque if __name__ == "__main__": es una construcción común en Python que se utiliza para determinar si un script se está ejecutando como el 
programa principal o si se está importando como un módulo en otro script.

¿Qué hace?
__name__:  En Python, cada módulo tiene un atributo especial llamado __name__.
Cuando un script se ejecuta directamente (como el programa principal), el valor de __name__ se establece en "__main__".
Si el script se importa como un módulo en otro script, el valor de __name__ se establece en el nombre del módulo.
if __name__ == "__main__":
Esta condición verifica si el script se está ejecutando como el programa principal.
Si la condición es verdadera, el código dentro del bloque if se ejecuta.
Si la condición es falsa (el script se está importando como un módulo), el código dentro del bloque if no se ejecuta.
¿Para qué se utiliza?

Ejecución de código específico:
El bloque if __name__ == "__main__": se utiliza para colocar el código que deseas que se ejecute solo cuando el script se ejecuta directamente.
Esto es útil para:
Probar funciones y clases en tu script. 
Ejecutar el código principal de tu programa.
Evitar que el código de prueba o el código principal se ejecute cuando el script se importa como un módulo.
Modularidad:
Permite que tus scripts sean tanto ejecutables como importables.
Puedes definir funciones y clases en tu script y luego importarlas en otros scripts para utilizarlas.
El bloque if __name__ == "__main__": asegura que el código de prueba o el código principal no interfiera con el código que se importa.

'''
