''' FUNCIONES LAMBDA'''

#? lambda son funciones sin nombre...anonimas . si acaso el "nombre" es lambda pero no estan definidadas como "def nombre(parametros):""
#? La sintaxis es :  " lambda argumentos:expresion " 
#? lambda es palabra reservada , argumentos son los parametros de la funcion y la expresion es corta y usa los argumentos

'''DEFINICION DE UNA FUNCION NORMAL PARA ELEVAR UN NUMERO AL CUADRADO'''

def elevar_al_cuadrado(numero):
    return numero*numero


numero=5
print(f"El cuadrado del numero {numero} es : {elevar_al_cuadrado(numero)}")

cuadrado= lambda numero: numero ** 2
print(f"El cuadrado del numero {numero}, es  {cuadrado}")