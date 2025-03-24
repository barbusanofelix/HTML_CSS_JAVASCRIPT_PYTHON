
import math

class Trefilado:
    def __init__(self, diametro_inicial, diametro_final, num_pasos, reduccion_inicial_1, reduccion_inicial_2):
        self.diametro_inicial = diametro_inicial
        self.diametro_final = diametro_final
        self.num_pasos = num_pasos
        self.reduccion_inicial_1 = reduccion_inicial_1 / 100.0
        self.reduccion_inicial_2 = reduccion_inicial_2 / 100.0
        self.diametros = []
        self.reducciones_area = []

    def calcular_serie(self):
        area_inicial = math.pi * (self.diametro_inicial / 2) ** 2
        area_actual = area_inicial

        # Primer paso (reducción fija)
        area_anterior = area_actual
        area_actual *= (1 - self.reduccion_inicial_1)
        diametro_actual = 2 * math.sqrt(area_actual / math.pi)
        self.diametros.append(diametro_actual)
        self.reducciones_area.append(self.reduccion_inicial_1 * 100)

        # Segundo paso (reducción fija)
        area_anterior = area_actual
        area_actual *= (1 - self.reduccion_inicial_2)
        diametro_actual = 2 * math.sqrt(area_actual / math.pi)
        self.diametros.append(diametro_actual)
        self.reducciones_area.append(self.reduccion_inicial_2 * 100)

        # Tercer paso (reducción fija del 24%)
        reduccion_tercer_paso = self.reduccion_inicial_2 - 0.01  # 24%
        area_anterior = area_actual
        area_actual *= (1 - reduccion_tercer_paso)
        diametro_actual = 2 * math.sqrt(area_actual / math.pi)
        self.diametros.append(diametro_actual)
        self.reducciones_area.append(reduccion_tercer_paso * 100)

        # Pasos restantes (reducción decreciente lineal ajustada)
        area_final = math.pi * (self.diametro_final / 2) ** 2
        pasos_restantes = self.num_pasos - 3

        # Calcular el decremento basado en la diferencia de áreas
        decremento_area = (area_actual - area_final) / pasos_restantes

        for _ in range(pasos_restantes):
            area_anterior = area_actual
            area_actual -= decremento_area
            diametro_actual = 2 * math.sqrt(area_actual / math.pi)
            self.diametros.append(diametro_actual)
            self.reducciones_area.append((area_anterior - area_actual) / area_anterior * 100)

        # Ajuste final para asegurar el diámetro final exacto
        self.diametros[-1] = self.diametro_final
        self.reducciones_area[-1] = (1 - area_final / (math.pi * (self.diametros[-2] / 2) ** 2)) * 100

        return self.diametros, self.reducciones_area

    def imprimir_resultados(self):
        diametros, reducciones_area = self.calcular_serie()
        print("Resultados del trefilado:")
        print("Paso\tDiámetro (mm)\tReducción de Área (%)")
        for i in range(self.num_pasos):
            print(f"{i + 1}\t{diametros[i]:.3f}\t\t{reducciones_area[i]:.2f}")
        print(f"Diametro final: {diametros[-1]:.2f} mm")

# Ejemplo de uso
diametro_inicial = 5.50
diametro_final = 2.17
num_pasos = 8
reduccion_inicial_1 = 20
reduccion_inicial_2 = 25

trefilado = Trefilado(diametro_inicial, diametro_final, num_pasos, reduccion_inicial_1, reduccion_inicial_2)
trefilado.imprimir_resultados()