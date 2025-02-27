letras = list('abcdefghijklmnopqrstuvwxyz')


cantidadLetras = len(letras)
contador=0
for c in letras:
    if contador>=int(cantidadLetras/3):# Mayor los imprimo en una linea
        print(c, end=' ')
    else:
        print(c) # <Cantidad de letras/3 las imprimo en cada linea     
    contador+=1


# Versión Pythónica. Más legible y rápido