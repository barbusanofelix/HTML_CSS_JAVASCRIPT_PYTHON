Lista=list()
Set = set()
print()
listCant = int(input(" Cantidad de elementos en la lista : "))
setCant =  int(input(" Cantidad de elementos en el Set   : "))
print()
# Introducir elementos en la Lista ( List )
print("Introduccion de datos de la Lista.")
for elemento in range(0,listCant):
    # list usa .append para añadir 
    Lista.append(input(f"Introduce el elemento {elemento+1} : "))  # Para que muestre empezando por 1 ( elemento + 1)
print()
print("Introduccion de datos del Set")
for elemento in range(0,setCant):
    # set usa .add para añadir
    Set.add(input(f"Introduce el elemento {elemento+1} : ")) 
    
print()
print("La lista introducida es :",Lista)  
print("El Set introducido es   :", Set)  