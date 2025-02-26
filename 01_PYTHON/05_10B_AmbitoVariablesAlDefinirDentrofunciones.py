G = 'Esta variable es de ámbito Global'
def f1():
    E="Esta variable es local a f1."    
#Enclosing a f2'
    def f2():
        L = 'L es local a f2'
        E = 'E tambien es local a f2'
        G = 'G tambien es local a f2. No considera la G global'
        print(L, E, G, sep = '\n')
    f2()
f1()