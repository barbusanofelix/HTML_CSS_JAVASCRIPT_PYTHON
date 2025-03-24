from math import pi

def area(r):
    #Verificamos los tipos correctos
    if type(r) not in [float, int]:
        raise TypeError("Solo números enteros o de coma flotante.")
    if r<0:
        raise ValueError("No se permiten valores negativos")
    areaC = pi*(r**2)
    return areaC


area_entero = area(3)
area_negativo= area(-3)
area_string=area("a")

print(area_entero, area_negativo, area_string)



