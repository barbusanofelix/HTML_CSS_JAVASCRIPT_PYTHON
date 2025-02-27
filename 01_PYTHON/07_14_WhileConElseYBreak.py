# El else en bucle while se ejecuta cuando el bucle se ejecuto limpiamente ( No uso el break) 

a = 291
b = a // 2 # División entera. P. ej. 13 // 2 == 6
while b > 1:
    if a % b == 0: # % es el operador resto. P. ej. 10 % 5 == 0
        print('{b} es factor de {a} y por tanto {a} no es primo'.format(b=b,a=a))
        break
    b -= 1
else:
        print('{} es primo'.format(a))

print ('\nFuera del Bucle.')

