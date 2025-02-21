def obtener_numeros():
    while True:
        entrada = input("Ingrese 2 números (a,b) separados por \", \": ")
        try:
            a, b = map(float, entrada.split(","))  # Usa float en lugar de int
            return a, b
        except ValueError:
            print("¡Error! Debe ingresar dos números válidos separados por \", \". Intente de nuevo.")
        except AttributeError: # por si no se ingresan dos valores separados por coma
            print("¡Error! Debe ingresar dos números separados por \", \". Intente de nuevo.")

def obtener_operador():
    while True:
        operador = input("Ingrese Operador (+,-,*,/) :")
        if operador in ("+", "-", "*", "/"):
            return operador
        else:
            print("¡Error! Debe ingresar un operador válido (+, -, *, /). Intente de nuevo.")

# Entrada toma el texto en la pantalla
a, b = obtener_numeros()
operador = obtener_operador()

print()
print("a= ", a)
print("b= ", b)
print("Operador :", operador)
print()
dec=2

print("Resultado :")
match operador:
    case "+":
        print(f"{a} + {b} = {a+b}")  # Usando f-string para formatear la salida
    case "-":
        print(f"{a} - {b} = {a-b}")  # Usando f-string para formatear la salida
    case "*":
        print(f"{a} * {b} = {a*b:.3f}")  # Usando f-string y formateo de decimales
    case "/":
        if b != 0:  # Simplificando la condición de división por cero
            print(f"{a} / {b} = {a/b:.3f}")  # Usando f-string y formateo de decimales
        else:
            print("¡Error! División por cero.")
    case _:
        print("Hay un error en los datos introducidos. Vuelva a correr y ponga atención en los datos que introduce.")
