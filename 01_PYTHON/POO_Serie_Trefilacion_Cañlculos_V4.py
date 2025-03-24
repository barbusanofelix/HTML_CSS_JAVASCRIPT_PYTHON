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
    deformacion_paso_1 = 1 - (diametro_paso_1 / Di) ** 2
    deformaciones.append(deformacion_paso_1)
    resultados.append((1, diametro_paso_1, Reduccion_1, deformacion_paso_1))

    # Calcular diámetro después del segundo paso
    area_paso_2 = area_paso_1 * (1 - Reduccion_2 / 100)
    diametro_paso_2 = 2 * math.sqrt(area_paso_2 / math.pi)
    diametros.append(diametro_paso_2)
    deformacion_paso_2 = 1 - (diametro_paso_2 / diametro_paso_1) ** 2
    deformaciones.append(deformacion_paso_2)
    resultados.append((2, diametro_paso_2, Reduccion_2, deformacion_paso_2))

    # Calcular los diámetros intermedios con reducción decreciente (usando diametro_paso_2 como materia prima)
    diametro_actual = diametro_paso_2
    reduccion_actual = Reduccion_2
    for i in range(3, Pases):
        reduccion_actual = reduccion_actual * 0.95  # Reducción decreciente (ajustar el factor si es necesario)
        area_actual = math.pi * (diametro_actual / 2) ** 2
        area_siguiente = area_actual * (1 - reduccion_actual / 100)
        diametro_siguiente = 2 * math.sqrt(area_siguiente / math.pi)
        diametros.append(diametro_siguiente)
        deformacion_paso = 1 - (diametro_siguiente / diametro_actual) ** 2
        deformaciones.append(deformacion_paso)
        resultados.append((i, diametro_siguiente, reduccion_actual, deformacion_paso))
        diametro_actual = diametro_siguiente

    # Asegurar la reducción del 16% en el último paso
    area_penultimo = math.pi * (diametros[-1] / 2) ** 2
    area_final = math.pi * (Df / 2) ** 2
    reduccion_final_calculada = (1 - area_final / area_penultimo) * 100
    deformacion_final = 1 - (Df / diametros[-1]) ** 2
    resultados.append((Pases, Df, reduccion_final_calculada, deformacion_final))
    deformaciones.append(deformacion_final)

    # Calcular deformación total
    deformacion_total = 1 - (Df / Di) ** 2

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