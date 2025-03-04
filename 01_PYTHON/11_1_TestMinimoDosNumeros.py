
'''
Dados 2 numeros encontrar el minimo de ellos

'''
print("Dados 2 numeros indica cual es el minimo de ellos")
a= int(input(" Numero 1 :"))
b= int(input(" Numero 2 :"))

min=None
if a<b:
    print(f"{a} es menor que {b}")
    min=a
elif a==b:
    print(f"{a} es igual a {b}")
    min="Son iguales"
else:
    print(f"{a} es mayor {b}")
    min=b

print("En resumen el minimo es :", min)

