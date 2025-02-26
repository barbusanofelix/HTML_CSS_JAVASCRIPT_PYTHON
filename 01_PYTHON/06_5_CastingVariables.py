# Forzado de tipo, CASTING:


# Forzado de tipo Enteros:
x = int(1)      # x Valdrá 1  Lo deja igual al ser entero
y = int(2.8)    # y Valdrá 2. Decimal : Lo Redondea a entero menor
z = int("3")    # z Valdrá 3. String a entero


# Forzado de tipo Float:
x = float(1)        # x Valdrá 1.0.  A un entero le agrega parte decimal
y = float(2.8)      # y Valdrá 2.8   A un decimal lo deja igual
z = float("3")      # z Valdrá 3.0   A un String entero lo pasa a numero decimal ( claro, era "3")
w = float("4.2")    # w Valdrá 4.2   A un string decimal lo pasa a decimal


# Forzado de tipo string:
x = str("s1")   # x Valdrá 's1'     Asegura que s1 sea un string.      
y = str(2)      # y Valdrá '2'      Convierte el numero 2 a un string
z = str(3.0)    # z Valdrá '3.0'    Convierte el decimal 3.0 a string


# CASTING. Reconversión de tipos:

# Casting de int a float:
n_numero = 13   
n_numero_2 = float(n_numero)    # Convierte el 13 a 13.0 ( Entero -> Decimal)
# Casting de float a int:   
n_numero_3 = 24.876             
n_numero_4 = int(n_numero_3)    # convierte 24.876 a 24
# Casting de string a int
s_texto = "13"
n_numero_5 = int(s_texto)       # convierte el 13 en texto a 13 entero. 
# Casting de int a string
n_numero_6 = 27
s_texto_2 = str(n_numero_6)     # convierte el entero 27 a texto 27
print(n_numero_2,end=" ")
print(type(n_numero_2))
print(n_numero_4,end=" ")
print(type(n_numero_4))
print(n_numero_5, end=" ")
print(type(n_numero_5))
print(s_texto_2,end=" ")
print(type(s_texto_2))