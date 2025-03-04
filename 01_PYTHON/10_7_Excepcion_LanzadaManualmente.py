
def iterador(objeto,indice):
    return objeto[indice]

def error(ite, longEntrada):
    if ite>(longEntrada-1):
        try:
            raise IndexError("Excepcion manual al superar el indice")
        except:
            print("Capture mi propia excepcion")
            return True
    else:
        return False    

entrada = input("Suministra un nombre : ")
ite = int(input(f"Suministra un indice para obtener el caracter de {entrada} :"))

longEntrada=len(entrada)  # obtener la longitud del string

if not error(ite,longEntrada):
    c=iterador(entrada, ite)
    print(c)
else:
    print("Indice muy grande")            

   