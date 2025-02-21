# Divisores en forma decrecientes de un numero n 


# Ingremos n por pantalla y convertimos el n, que esta en texto, a entero con int()
n = int(input("Ingrese el número para hayar sus divisores: "))
print()

#  Concatenando con el "+". Hay que reconvertir a String la n con str(n)
print("Los divisores de : "+ str(n)+" en orden decreciente, son:")

# Los divisores estan en 1 a Raiz Cuadrada de n y luego el valor de n
hastaMitad_n = int(n/2)  # Toma la parte entera de la raíz cuadrada


print( str(n)+" - ", end="")  # end="" evita el salto de linea.
for i in range(hastaMitad_n,1, -1):  # Va desde hastaMitad_n hasta >0 ( 1) reduciendo 1 
    if(n % i==0):
        print( str(i) + " - ", end="")   # end="" evita el salto de linea
    
print( 1 )
    

