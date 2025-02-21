# Programa para operaciones basicas con 2 numeros ( a y b )
# Operacion basica ( Op ) son +, -, * y /

#Funciones
def obtener_numeros():
    while True:
        entrada = input("Ingrese 2 números (a,b) separados por \", \": ")
        try:
            a, b = map(float, entrada.split(","))  # Usa float en lugar de int
            return a, b
        except ValueError:
            print("¡Error! Debe ingresar dos números válidos separados por \", \". Intente de nuevo.")
        

def obtener_operador():
    while True:                                     # True con mayuscula
        operador=input("Ingrese Operador ( +,-,*,/) :")
        if operador in ("+", "-", "*", "/"):
            return operador
        else:
            print("¡Error! Debe ingresar un operador válido (+, -, *, /). Intente de nuevo.")

def decimal_suma():
    if isinstance(a, int) and isinstance(b, int):
        decimales=0
        return decimales
    else:
        decimales=3
        print("Funcion suma")
        return decimales

def enteroOrFloat(valor):
    if (valor%1==0):
        valor=int(valor)
    else:
        valor=valor
        return valor
    


#Entrada toma el texto en la pantalla
a,b = obtener_numeros()
a=enteroOrFloat(a)
b=enteroOrFloat(b)
operador = obtener_operador()

        
 

# Determina la cantidad de decimales según el tipo de datos de a y b y la división
if isinstance(a, int) and isinstance(b, int):
    decimales=0
    if b == 0:
        #print("Error: No se puede dividir por cero.")  # Manejo de división por cero
        decimales = 0  # Se deja en cero para que no de error
    else:
        resultado_division = a / b  # División de punto flotante
        if resultado_division < 1 and resultado_division != int(resultado_division):
            decimales = 3
        else:
            decimales = 0  # Mostrar decimales siempre en la división
else:
    decimales = 3  # Si a o b no son enteros, mostrar 3 decimales


print()
print("a= ", a)
print("b= ", b)
print("Operador :", operador)
print()
print("decimales ="+ str(decimales))    

print("Resultado :")
match operador:
    case "+":
        dec=decimal_suma()
        print("La funcion devolvio="+str(dec))
        print(f"{a} + {b} = {a+b:.{dec}f}")
    case "-":
        print(str(a) + " - "+ str(b) + " = "+ str(a-b))
    case "*":
        print(f"{a} * {b} = {a*b:.{decimales}f}")       # f para la sustitucion de la a y b entre {} y luego .3f para los 3 decimales
    case "/":
        if (a*b!=0):                                    # != distinto de cero
            print(f"{a} / {b} = {a/b:.{decimales}f}")   # f para la sustitucion de la a y b entre {} y luego .3f para los 3 decimales
        else:
            if (a==0 and b==0):
                print("Resultado NaN, division de 0/0")
            else:
                if(a!=0 and b==0):
                    print("Infinito, division por cero!!")
                else:
                    if(a==0 and b!=0):
                        print(f"{a} / {b} = {a/b:.{decimales}f}")       # f para la sustitucion de la a y b entre {} y luego .3f para los 3 decimales
    case _:
        print("Hay un error en los datos introducidor. Vuelve a correer y pon atencion en los datos que introduces")




