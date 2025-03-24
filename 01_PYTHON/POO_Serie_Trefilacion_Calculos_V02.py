def PorcRedConDiam(do, df):
    return (1 - pow(df / do, 2)) * 100

def deforPorPase(do, df, pases):
    return pow((df / do), (1 / pases))

def df_vs_do_defor(diametro_anterior, deforCte):
    return diametro_anterior * deforCte

def calculoSerieDeforCte(do, df, pases):
    serie = []
    serie.append((do, 0))  # Inicializa con el diámetro original y 0% de reducción
    deforCte = deforPorPase(do, df, pases)
    for i in range(1, pases + 1):
        diametro_actual = round(df_vs_do_defor(serie[i - 1][0], deforCte), 3)
        porcentaje_reduccion = round(PorcRedConDiam(serie[i - 1][0], diametro_actual), 2)
        serie.append((diametro_actual, porcentaje_reduccion))
    return serie

def imprimir_tabla_trefilacion(serie):
    print("Pase\tDiámetro (mm)\t% Reducción")
    print("-" * 40)
    for i, (diametro, porcentaje) in enumerate(serie):
        print(f"{i}\t{diametro:.2f}\t\t{porcentaje:.2f}")

# Ejemplo de uso
do = 6.35
df = 2.031
pases = 8

serie_trefilacion = calculoSerieDeforCte(do, df, pases)
imprimir_tabla_trefilacion(serie_trefilacion)