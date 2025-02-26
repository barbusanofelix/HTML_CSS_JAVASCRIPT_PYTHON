#FUNCONES ANIDADAS


def f1(a):          # Función que "encierra a f2 (enclosing)
    print(a)        # Se imprimira Python
    b = 100         # b=100
    def f2(x):      # Función anidada f2 dentro de f1 ( misma indentacion)
        print(x)    # Imprimira x que valdra 100 pues es lo que recibe en parametro.
# Llamamos a f2 dentro de f1. Al estar dentro b=100 asi que a f2 le enviamos 100
    f2(b)      # f2 esta definida previamente para que la encuentre.  

# Llamamos a f1
f1('Python') 

# Fuera de f1 , f2 No es visible.