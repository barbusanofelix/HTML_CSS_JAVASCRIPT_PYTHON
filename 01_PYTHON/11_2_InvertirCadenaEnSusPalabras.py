
print("Invertir las palabras de una cadena")
cadena= input("Suministra una frase : ")

palabras =list()
palabras = cadena.split(" ")

cadenaSalida = ""
for palabra in reversed(palabras):
    cadenaSalida +=palabra+" "

print(cadenaSalida)     