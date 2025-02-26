G = 'G:Esta variable es de ambito Global'
def f1():
    E='E:Esta variable es local a f1.'

#Enclosing a f2'
    def f2():
        L = 'L:Esta variable es local a f2'
        print("Aqui las 3 variables L, E, G",L, E, G, sep = '\n')
    f2() # Hay que llamarla asi misma despues de definirla
f1()    