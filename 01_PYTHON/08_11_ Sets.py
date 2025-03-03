# SETs, conjuntos
"""
Un conjunto es una colección de elementos únicos que no está ordenada ni indexada, por lo que no puede 
estar seguro de en qué orden aparecerán los elementos.
En Python, los conjuntos se escriben entre llaves.

Una vez que se crea un conjunto, no puede cambiar sus elementos, pero puede agregar
nuevos elementos.
"""
print()
# Declaración:
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo","Juan"}
# Otra forma de declararlo
mi_conjunto3 = set(("Angel", "Sara","Pilar"))
print('1. Creando un set con mi_conjunto3 = set(("Angel", "Sara","Pilar"))',mi_conjunto3)
print()
print('2. Otra forma de crear es con mi_conjunto = {"Angel", "Sara", "Pilar"}')
# Para añadir un nuevo elemento:
mi_conjunto.add("Antonio")
print()
print('3. Añadir un elemento con mi_conjunto.add("Antonio") ', mi_conjunto)
# Para añadir varios elementos:
mi_conjunto.update({"Fran", "María"})
print()
print('4. Añadir varios elementos con mi_conjunto.update({"Fran", "María"})',mi_conjunto)
# Unión de colecciones. Si hay algún valor repetido sólo aparecerá una vez.
print()
print("Union de colecciones")

union= mi_conjunto | mi_conjunto2
print("5. union= mi_conjunto | mi_conjunto2", union)
# Intersección de conjuntos:
interseccion= mi_conjunto & mi_conjunto2
print("6. interseccion= mi_conjunto & mi_conjunto2", interseccion)
# Nos crea otro conjunto con los valores que estaban duplicados en ambos conjuntos.
# En nuestro caso sólo Angel.
# Diferencia de conjuntos. Nos crea otro conjunto con los elementos que no están duplicados.
diferencia= mi_conjunto - mi_conjunto2
print()
print("La diferencia de conjunto crea un conjunto eliminando los repetidos")
print("7. Diferencias de conjuntos , diferencia= mi_conjunto - mi_conjunto2 ", diferencia);print()
# Para comprobar si un elemento está en un conjunto:
angelpresente="Angel" in mi_conjunto # Devuelve true o false
print("8. Para si un elemento esta : Angel in mi_conjunto, y devuelve True o False", angelpresente)
print()
# Recorra el conjunto e imprima los valores: 
miSet = {"manzana", "banana", "cereza"}
print("9. Recorre en Set con 'for fruta in miSet:'")
for fruta in miSet:
    print(fruta)
"""
No puede acceder a los elementos de un conjunto haciendo referencia a un índice, ya que los conjuntos no 
están ordenados, los elementos no tienen índice.
"""
# Obtenga la cantidad de elementos en un conjunto:
print("Obtener la cantidad de elementos en un conjunto")
miSet = {"manzana", "banana", "cereza"}
print(len(miSet))
print("10. Cantidad de elementos len(miSet)", len(miSet));print()
# Elimine "banana" utilizando el método remove() :
miSet = {"manzana", "banana", "cereza"}
miSet.remove("banana")
print('11. Remueve elemento del Set, con miSet.remove("banana")',miSet);print()
# Elimine "banana" utilizando el método discard() :
miSet = {"manzana", "banana", "cereza"}
miSet.discard("banana")
print('12.Remover con miSet.Discart("banana"): ',miSet)
print("Discard no genera error si el elemento no existe PERO remove SI GENERA UN ERROR")
"""
Si el elemento a eliminar no existe, remove() generará un error.
Si el elemento a eliminar no existe, discard() NO generará un error.
"""