
t=(7,8,9,1,10,8)


def sumaTupla(t):
    suma=0
    for n in t:
        suma+=n
    return suma



if __name__=="__main__":
    print("La tupla es", t)
    print(sumaTupla(t))
