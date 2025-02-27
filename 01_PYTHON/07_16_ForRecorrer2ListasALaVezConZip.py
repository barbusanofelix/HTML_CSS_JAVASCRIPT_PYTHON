la = [10, 20, 30, 40]
lb = [5, 25, 50, 10,100]  # la lista lb tiene un elemento mas que la lista la


# zip crrea un iterador para recorrer en simultaneo las 2 listas. 
# El iterador llega solo hasta la lista mas pequeña.
# Como lb tiene un elemento adicional ( 100 ) simplemente no se toma en cuenta
# y se recorre hasta el 40 de la lista la
for a, b in zip(la, lb):  # recorre la lista la y lb a la vez
    m = max(a, b) # max(a, b),  devuelve el máximo entre la y lb
    print(m , end=" ")          # imprim

# salida    
# 10 25 50 40