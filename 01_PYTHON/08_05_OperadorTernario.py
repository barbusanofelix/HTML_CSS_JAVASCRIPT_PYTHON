# Operador ternario
print("Operador ternario")

num = 13

var = "par" if (num % 2 == 0) else "impar"   # varifica si el modulo es cero = par, si no es cero = impar
print(f"La variable {num} es {var}")
# Sería como escribir
num = 12
if num % 2 == 0:
    print="Par"
else: print="Impar"