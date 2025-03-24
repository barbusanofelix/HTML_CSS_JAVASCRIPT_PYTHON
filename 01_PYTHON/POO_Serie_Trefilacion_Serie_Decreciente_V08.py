import math

def calcular_trefilacion(Di, Df, Pases, Reduccion_1, Reduccion_2, Reduccion_final):
    """
    Calcula la serie de trefilación con reducciones de área especificadas.

    Args:
        Di: Diámetro inicial (mm).
        Df: Diámetro final (mm).
        Pases: Número de pasos.
        Reduccion_1: Reducción de área del primer paso (%).
        Reduccion_2: Reducción de área del segundo paso (%).
        Reduccion_final: Reducción de área del último paso (%).

    Returns:
        Una lista de tuplas con los resultados (paso, diámetro, porcentaje de reducción, deformación).
    """

    resultados = [(0, Di, 0, 0)]  # Incluir el diámetro inicial como Paso 0
    diametros = [Di]  # Almacena los diámetros en cada paso
    deformaciones = [0]  # Almacena las deformaciones en cada paso

    # Calcular diámetro después del primer paso
    area_inicial = math.pi * (Di / 2) ** 2
    area_paso_1 = area_inicial * (1 - Reduccion_1 / 100)
    diametro_paso_1 = 2 * math.sqrt(area_paso_1 / math.pi)
    diametros.append(diametro_paso_1)
    deformacion_paso_1 = math.log(area_inicial / area_paso_1)
    deformaciones.append(deformacion_paso_1)
    resultados.append((1, diametro_paso_1, Reduccion_1, deformacion_paso_1))

    # Calcular diámetro después del segundo paso
    area_paso_2 = area_paso_1 * (1 - Reduccion_2 / 100)
    diametro_paso_2 = 2 * math.sqrt(area_paso_2 / math.pi)
    diametros.append(diametro_paso_2)
    deformacion_paso_2 = math.log(area_paso_1 / area_paso_2)
    deformaciones.append(deformacion_paso_2)
    resultados.append((2, diametro_paso_2, Reduccion_2, deformacion_paso_2))

    # Calcular deformación del último paso
    area_final = math.pi * (Df / 2) ** 2
    area_penultimo = area_final / (1 - Reduccion_final / 100)
    diametro_penultimo = 2 * math.sqrt(area_penultimo / math.pi)
    deformacion_final = math.log(area_penultimo / area_final)
    deformaciones.append(deformacion_final)

    # Calcular la deformación restante y distribuirla con progresión aritmética
    deformacion_restante = math.log(area_paso_2 / area_final) - deformacion_final
    suma_pasos_restantes = sum(range(1, Pases - 2))
    deformacion_incremento = deformacion_restante / suma_pasos_restantes

    # Calcular los diámetros intermedios y las deformaciones
    diametro_actual = diametro_paso_2
    for i in range(3, Pases - 1): # Modificado para llegar hasta el paso 7
        deformacion_paso = deformacion_final + (Pases - i - 1) * deformacion_incremento
        area_actual = math.pi * (diametro_actual / 2) ** 2
        area_siguiente = area_actual / math.exp(deformacion_paso)
        diametro_siguiente = 2 * math.sqrt(area_siguiente / math.pi)
        diametros.append(diametro_siguiente)
        deformaciones.append(deformacion_paso)
        reduccion_actual = (1 - area_siguiente / area_actual) * 100
        resultados.append((i, diametro_siguiente, reduccion_actual, deformacion_paso))
        diametro_actual = diametro_siguiente

    # Asegurar la reducción del 16% en el último paso
    resultados.append((Pases - 1, diametro_penultimo, (1 - area_final/area_penultimo) * 100, deformacion_final)) # Añadido paso 7 con los datos correctos
    resultados.append((Pases, Df, Reduccion_final, deformacion_final))

    # Calcular deformación total
    deformacion_total = math.log(area_inicial / area_final)

    return resultados, deformacion_total

# Entrada de datos del usuario
Di = float(input("Ingrese el diámetro inicial (mm): "))
Df = float(input("Ingrese el diámetro final (mm): "))
Pases = int(input("Ingrese el número de pasos: "))
Reduccion_1 = float(input("Ingrese la reducción del área del primer paso (%): "))
Reduccion_2 = float(input("Ingrese la reducción del área del segundo paso (%): "))
Reduccion_final = float(input("Ingrese la reducción del área del último paso (%): "))

# Calcular y mostrar resultados
resultados, deformacion_total = calcular_trefilacion(Di, Df, Pases, Reduccion_1, Reduccion_2, Reduccion_final)

print("\nResultados de la trefilación:")
print("Paso\tDiámetro (mm)\tReducción (%)\tDeformación")
for paso, diametro, reduccion, deformacion in resultados:
    print(f"{paso}\t{diametro:.4f}\t\t{reduccion:.2f}\t\t{deformacion:.4f}")

print(f"\nDeformación total: {deformacion_total:.4f}")