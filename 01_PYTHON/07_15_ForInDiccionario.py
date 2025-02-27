keys   = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values)) # Creamos el diccionario juntando 
print(d)



for k in d:                             # K corresponde a la key
    info = '{}: {}'.format(k, d[k])     # crea una pareja clave-valor
    # Texto formateado con claves y valores
    print(info)                         # Imprime la pareja clave-valor
    #Apellidos: van Rossum
    #edad: 60
    #nombre: Guido
print("Fin del for in diccionario")