def minimo(a,b):
    if a<=b:
        return a
    else:
        return b

print("Suminsitra dos numeros para determinar el menor")    
a= int(input(" a = "))
b= int(input(" b = "))

print("El minimo es :", minimo(a,b))
