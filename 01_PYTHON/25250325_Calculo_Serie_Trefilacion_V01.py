import math as m



def deforEntrePases(do,df):                 #* Calcula la deformacion Total entre pases ( Puede ser entre cualquier tramo )
    return 2*m.log(do/df)

def PorcRedConDiam(do,df):                  #* Calcula el Porcentaje Reduccion en base a los Diametros ( Porc= Porcentaje, Red=Reduccion ConDiam = Con diametros)
    return (1-pow(df/do,2))*100             

def PorcRedConDefor(deformacion):           #* %Red =(1-EXP(-Et))*100 , Et= Defomacion ( deformacionEntrePases(do,df): )
    return (1-pow(m.e,-deformacion))*100  

def df_vs_do_defor(do,deformacion):         #* Calcula el diametro siguiente ( De arriba hacia abajo, descendiente ) para la deformacion  Df=Do*EXP(-Et/2) ...recuerda que EXP es "e" elevado a -Et/2
    return do*pow(m.e,-deformacion/2)

def do_vs_df_defor(df,deformacion):         #* Calcula el diametro previo ( de abajo hacia arriba  )dando el diametro final y la deformacion        
    return df/(pow(m.e,deformacion))

def deforPorPase(do,df,pases):              #* Calcula la deformacion promedio entre pases....Puede ser toda la serie o entre cualquier numero.
    deforEntreDoDf= deforEntrePases(do,df)  #! Esta deformacion se puede usar para el calcuo de serie con deformacion constante.
    return deforEntreDoDf/pases
    

def factSecuenciaRed(pases):               # Facot secuencia de reduccion .
    fsr=0
    for n in range(1, pases):           #* Es un factor para distribuir la reduccion desde el ultimo pase al primero.
        fsr+=pases-n                    #* Siendo n el numero de pases es la suma de facSecuenciaRed= (n-1)+(n-2)+(n-3) .....1 
    return fsr

def deforUnPase(reduccion):             #* Sirve para calculo deformacion dando % Reduccion como el ultimo pase            
    return m.log(1/(1-reduccion/100))

def deforEi(do,df,pases,redUltPase):            # Deformacion Individual ( e_i)  y e_i se forma parte de a repartir en los pasos ( "ei"  junto con la "en" ) e=deformacion, i= "integrada" 
    DeforTotal = deforEntrePases(do,df)         # Calcula la deformacion total en el rango de diametros que queremos hacer la serie decreciente.
    n=pases                                     # Numero de pases entre la region que queremos colocar la serie decreciente.
    fsr=factSecuenciaRed(pases)                 # Obtenemos el factor de para distribuir la reduccion en forma homogenea en los pasos
    deforUltPase=deforUnPase(redUltPase)        # Pasamos la reduccion para el ultimo pase.  
    e_individual=(DeforTotal-pases*deforUltPase)/fsr
    return  e_individual                                  # La reduccion a distribuir por los pases

def deforPaseDec(pases, ei, e_ult_pase):                # Deformacion por Pase Decreciente. Parametros: Numero Pases ( pases ), deformacion individual para  repartir en los pases 
    e_pase=[]                                   # (ei =deforEi) y e_ult_pase e=Deformacion ultimo pase) 
    e_pase.append(0)                            # Deformacion por pase
    et=0
    for i in range(1,pases+1):
        e_pase.append(e_ult_pase+ei*(pases-i))
    return e_pase                                   # ep= Deformacion por pase.
                                                # CON ESTA LISTA, QUE CONTIENE LA DEFORMACION DECRECINTE SE CALCULA LA SERIE DECRECIENTE CONDICIONADA POR LA REDUCCION DEL ULTIMO PASE

def verificacion_et(ep,do,df,pases):                  # Verifica si la deformacion Total obtenida de los pases es igual a la et obtenida por do a df (deforEntrePases(do,df):
    et_diam=deforEntrePases(do,df)              # et obtenida por do a df    
    et_def_ep=0
    for i in range(1,pases+1):
        et_def_ep+=ep[i]
    diferencia_et= et_def_ep-et_diam
    return diferencia_et


def calculoSerieDeforCte(do, df, pases):        # CALCULO SERIE DEFORMACION CONSTANTE ( % REDUCCION IGUAL PARA TODOS LOS PASES
    serie = []
    serie.append((do, 0, 0))                         # Colocamos el diametro del pase ( siendo el pase p), %Reduccion entre el pase p-1 y pase p, deformacion entre p-1 y pase p.  Inicializa con el diámetro original y 0% de reducción, deformacion  en una Tupla
    deforCte = deforPorPase(do, df, pases)                                                  # Calculamos la deformacion constante al serie uniforme
    for n in range(1, pases + 1):                                                           # Hacemos un recorrido desde 1 hasta pases ( pases + 1 no lo incluye). El cero es para la M.Prima
        diametro_actual = round(df_vs_do_defor(serie[n - 1][0], deforCte), 3)               # Aplicamos el metodo de calcula el diametro actual en funcion del diametro en serie[i-1] ( anterior) y actual    
        porcentaje_reduccion = round(PorcRedConDiam(serie[n - 1][0], diametro_actual), 1)   # calculamos el porcentaje de reduccion
        serie.append((diametro_actual, porcentaje_reduccion,deforCte))                               # Añadimos a la seri el diametro actual y el porcentaje de reduccion. 
    return serie                                                                            # Devuelve la serie que en realidad es una Lista de Tupla ( Diametro y reduccion) 
    
def imprimir_serie_deforCte(serie,mensaje):                                 # Imprimir serie deformacion Contante.
    defor_total=0
    print()
    print(mensaje)                                                          # Para completar el mensaje de la serie.            
    print("Pase\tDiámetro (mm)\tReducción (%)\t Deformacion")
    print("-" * 40)
    for i, (diametro, porcentaje, deformacion) in enumerate(serie):
        if i == 0:  # Para el pase 0 (M.Pr)
            print(f"M.Pr\t{diametro:.2f}\t\t")  # Imprimir "M.Pr" y dejar en blanco la reducción
        else:
            print(f"{i}\t{diametro:.2f}\t\t{porcentaje:.2f} \t\t {deformacion:.4f}")  # Para los demás pases
            defor_total+= deformacion
    print(f"\nDeformacion acumulada : {defor_total:.4f}\n")
                                                
                                                
def calculoSerieDeforDecrMpr(do,e_pase, pases):            #do= Diametro Inicial, ep = deformacion por pase 
    serieDec=[]
    serieDec.append((do, 0, 0))                         # Colocamos el diametro del pase ( siendo el pase p), %Reduccion entre el pase p-1 y pase p, deformacion entre p-1 y pase p  
    for n in range(1,pases+1):                          # n inicia en 0 ( M.prima y pases+1 incluye < pases+1 , es decir , pases)
        df=df_vs_do_defor(serieDec[n-1][0],e_pase[n])       # 
        porcentaje_reduccion = PorcRedConDiam(serieDec[n - 1][0], df)  
        serieDec.append((df,porcentaje_reduccion,e_pase[n]))
    return serieDec

#? Determina cual debe ser el porcentaje maximo de reduccion en el ultimo pase para que la serie sea de reduccion decreciente.
#? Se puede fijar la reduccion del 1er pase, 2do pase y ultimo pase. La  idea es establecer cual es el porcentaje maximo en ultimo pase para 
#? que la serie sea decreciente, en funcion de los parametros de reducciones que le dimos en 1ero y 2do pase.
def minima_reduccion_ult_pase_serie_decreciente(do,df,pases,porc_red1, porc_red2):       #? do= Diametro inicial o el d2 ( diametro en 2do pase),df= diametro del pase final. 
    defor_p1=deforUnPase(porc_red1)
    d1=df_vs_do_defor(do,defor_p1)              # d1: diametro en pase 1
    defor_p2=deforUnPase(porc_red2)
    d2=df_vs_do_defor(d1,defor_p2)              # d2: Diametro en pase 2 
    defor_p3=defor_p2                           # Deformacion p3 es igual a la deformacion del pase 2 (aceptaria que el %Red del pase 3 sea igual al pase 2)
    d3=df_vs_do_defor(d2,defor_p2)              # d3: Se calcula en base al d2 y con la misma deformacion del pase 2 (misma reduccion)  
    e_total_d2=deforEntrePases(d2,df)           # Deformacion entre pase 2 al pase final.
    e_total_d3=deforEntrePases(d3,df)
    print("CALCULO REDUCCION MINIMA")
    print("deformacion p2: ", defor_p2, " e_total_d2_df : ", e_total_d2, "e_totl_d3_df : ", e_total_d3)
    
    # Base a formulas de reduccion obtengo la deformacion maxima en ultimo pase para que sea descendiente la serie.
    e_ult_pase_desde_d2 = (defor_p2*factSecuenciaRed(pases-2)-(pases-2)*e_total_d2)/(factSecuenciaRed(pases-2)-(m.pow(pases-2,2)))
    e_ult_pase_desde_d3 = (defor_p3*factSecuenciaRed(pases-3)-(pases-3)*e_total_d3)/(factSecuenciaRed(pases-3)-(m.pow(pases-3,2)))
    print("*****CALCULA e_pase2 x factor secuencias ", e_ult_pase_desde_d2)
    porc_max_ult_pase_desde_d2= 100*(1-m.pow(m.e,-e_ult_pase_desde_d2))
    porc_max_ult_pase_desde_d3= 100*(1-m.pow(m.e,-e_ult_pase_desde_d3))
    porc_max_d2_d3=(porc_max_ult_pase_desde_d2,porc_max_ult_pase_desde_d3)
    return porc_max_d2_d3
    
    
    
def calculoSerieDecrConRedDada1ero2doPase(do,df,pases,porc_red1, porc_red2, porc_red_ult_pase):        
    print(f"Parametros recibidos do {do} df {df} pases {pases} %Red_p1 {porc_red1} %red.p2 {porc_red2} %Red.Ultimo pase {porc_red_ult_pase} ")# calculo Serie Decrec con reduccion Dada en 1ero, 2do pase 
    serieDecRed1_2=[]                                              # Serie decreciente desde 3er a ultimo pase
    serieDecRed1_2=[(do,0,0)]
    
    defor_p1=deforUnPase(porc_red1)
    print("Deformacion pase 1 para red=20%", defor_p1)
    d1=df_vs_do_defor(do,defor_p1)
    print("d1 =", d1)
    serieDecRed1_2.append((d1,porc_red1,defor_p1))                  # No olvidar los parentisis de la Tupla.
    
    defor_p2=deforUnPase(porc_red2)
    d2=df_vs_do_defor(d1,defor_p2)
    print("d2:",d2)
    serieDecRed1_2.append((d2,porc_red2,defor_p2))
    
    # Ahora tengo que calcular una serie con reduccion decreciente donde el Do = d2 y los pasos serian pasos-2
    # Luego, tengo que añadir la serie obtenida desde el paso 1 hasta el paso final empezando desde la posicion 3 (Ya tengo añadio 0,1 y 2)
    # Primero calculo la deformacion de los pases.
    
    e_individual_repartida=deforEi(d2,df,pases-2,porc_red_ult_pase)
    
    e_total=deforEntrePases(d2,df)
    print("El e_toal desde d2 a df ", e_total)
    factor_secuencia=factSecuenciaRed(pases-2)
    
    print(f"Ei : {e_individual_repartida:.6f} d2: {d2:.4f}  df: {df:.3} pases:{pases-2} Fact_secuencia: {factor_secuencia:.2f}  e_total: {e_total:.6f}    ")
    
    e_ult_pase=deforUnPase(porc_red_ult_pase)
    e_pase= deforPaseDec(pases-2,e_individual_repartida,e_ult_pase)
    
    acumulado_defor =0
    for e in e_pase:
        print(f"Defor /pase) : {e:.6f}")
        acumulado_defor+=e
    print(" Deform acumulada: ", acumulado_defor)
    
    serie_faltante=[]
    for n in range(3,pases+1):     # Recorremos de 3 a 8 , solo que e_pase arranca en 0 y termina en 6
        df=df_vs_do_defor(d2,e_pase[n-2])
        porc_reduccion= PorcRedConDiam(d2,df)
        defor=e_pase[n-2]
        serie_faltante.append((df,porc_reduccion,defor))
        serieDecRed1_2.append((df,porc_reduccion,defor))
        d2=df
        
        
    print(serie_faltante)    
    
    return serieDecRed1_2



'''
Funcion para graficar metodo 2

'''  
import matplotlib.pyplot as plt
import tkinter

def graficar_serie(series, pases):
    import numpy as np

    #* CONVERTIMOS LOS ELEMENTOS DE LA SERIE EN VALORES X (PASE)  Y LOS Y ( DIAMETRO Y REDUCCION COMO FUNCION DE LOS PASES)
    pase = [i for i in range(0, pases + 1)]
    diametro = [serie[0] for serie in series]
    reduccion = [serie[1] for serie in series]

    if reduccion:                   #* # Si la lista de reducciones no está vacía
        reduccion[0] = None         #* Asignamos None a la reduccion[0] ( se corresponde con la M.Prima)

   
    #* Obtener la resolución de la pantalla
    ''' Crea una instancia de la clase Tk de tkinter. Tk es la ventana principal de una aplicación tkinter. 
        Aunque no se muestra visualmente en este caso, es necesario crearla para acceder a las propiedades de la pantalla.'''
    root = tkinter.Tk()
    
    '''
    Llama al método winfo_screenwidth() del objeto root. Este método devuelve el ancho de la pantalla en píxeles. 
    El valor obtenido se almacena en la variable screen_width.
    '''
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    '''
    Destruye la ventana Tk que se creó al principio. Esto es importante para liberar los recursos del sistema y evitar que la ventana 
    permanezca abierta innecesariamente.
    Destruye la ventana Tk que se creó al principio. Esto es importante para liberar los recursos del sistema y evitar que la ventana permanezca abierta innecesariamente.

    El código crea una ventana tkinter temporal, obtiene el ancho y el alto de la pantalla, imprime la resolución en la consola y luego destruye la 
    ventana temporal. Esto permite obtener la resolución de la pantalla sin mostrar una ventana visible al usuario.
    '''    
    root.destroy()

    #* Calcular el tamaño de la figura como un porcentaje de la pantalla
    width_inches = screen_width / 200  #100  # Ajusta el divisor para cambiar el porcentaje
    height_inches = screen_height / 200 # 100 # Ajusta el divisor para cambiar el porcentaje

    # Crear el grafico y los ejes ( >solo memoria. No se muestra hasta show())
    fig, ax1 = plt.subplots(figsize=(width_inches, height_inches)) # Establecer el tamaño de la figura

    #? Configurar el eje X
    ax1.set_xlabel("Numero de pase")
    #? Configurar el eje Y izquierdo (diámetro)
    ax1.set_ylabel("Diametro", color="blue")
    #? Graficar los diámetros
    ax1.plot(pase, diametro, color="blue", label="Diametros por paso")
    #? Configurar las marcas del eje Y izquierdo
    ax1.tick_params(axis="y", labelcolor="blue")
    #? Configurar los límites del eje Y izquierdo
    ax1.set_ylim(0, round(max(diametro)*1.25))                            #ax1.set_ylim(min(diametro) - 1, max(diametro) + 1)       # Una forma de suministrar el rango de diametros en el eje y

    # Agregar valores sobre los puntos del diametro.Valores formateados sobre los puntos del diametro.
    for i, txt in enumerate(diametro):
        ax1.annotate(f'{txt:.2f}', (pase[i], diametro[i])) # formato con 2 decimales.

    #? Crear el eje Y derecho (reducción)
    ax2 = ax1.twinx()

    ax2.set_ylabel("%Reducion entre pases", color="red")
    #? Graficar las reducciones
    ax2.plot(pase, reduccion, color="red", marker='o', label="%Reducion entre pases") # Marcadores circulares
    #? Establece el min y max de eje Y secuendario
    ax2.set_ylim(0, 50) # Establecer el rango del eje Y derecho de 0 a 50

    #? Agregar valores formateados sobre los puntos de la reduccion.
    reduccion_filtrada = [r for r in reduccion if r is not None]  #?# Se filtra para evitar errores con valores None.

    if reduccion_filtrada:
        # Agregar valores formateados sobre los puntos de la reduccion.
        for i, txt in enumerate(reduccion):
            if txt is not None:
                ax2.annotate(f'{txt:.2f}', (pase[i], reduccion[i]))
    else:
        print("Advertencia: No hay valores válidos para el eje de reducción.")
        
    # Agregar lineas verticales punteadas en cada pase
    for x in pase:
        ax1.axvline(x, color='gray', linestyle='--', linewidth=0.8) # lineas punteadas en eje izquierdo
        ax2.axvline(x, color='gray', linestyle='--', linewidth=0.8) # lineas punteadas en eje derecho    

    fig.suptitle("Gráfico Diametro y Reduccion por pase")
    #? Mostrar la leyenda
    fig.legend()
    plt.grid(True)
    plt.show()             
       
             
do=6.35
df=2.032
porc_red_pase1=22
porc_red_pase2=25
porc_red_ult_pase=18.96097802831117
pases=9
deforPase3Con26=deforUnPase(26)

porc_maximo_ult_pase_para_red_Decre= minima_reduccion_ult_pase_serie_decreciente(do,df,pases,porc_red_pase1, porc_red_pase2)  # devuelve Tupla de los porcentajes ultimo pase segun d2 y d3
porc_ideal_ult_pase_origen_d2, porc_ideal_ulto_pase_origen_d3= porc_maximo_ult_pase_para_red_Decre

print("Cual es el porcentaje minimo para hacer serie decreciente desde d2 : ", porc_ideal_ult_pase_origen_d2)
print("Cual es el porcentaje minimo para hacer serie decreciente desde d3 : ", porc_ideal_ulto_pase_origen_d3)

print("Deformacion para un pase dado %Red : ",deforPase3Con26  )

serie= calculoSerieDeforCte(do,df,pases)                           # Cacula serie de deformacion constante
imprimir_serie_deforCte(serie, "Deformacion Contante")

print(" Facor de secuencia de reduccion:", factSecuenciaRed(pases))

print(f" Deformacion dada un porcentaje de reduccion   {deforUnPase(16):.4f}")

e_individual_repartida=deforEi(do,df,pases,16)
e_ult_pase=deforUnPase(16)        # en=deforUnPase(16)  en= deformacion ultimo pase , e_ult_pase y le asignamos el % que queremos para ese pase.

e_pases=deforPaseDec(pases,e_individual_repartida,e_ult_pase)       # Devuelve la Lista de las deformaciones de todos los pases

print(e_pases[0])
print(e_pases)
print(f"Diferencia et {verificacion_et(e_pases,do,df,pases):.6f}")

serie_Decreciente= calculoSerieDeforDecrMpr(do,e_pases,pases)

imprimir_serie_deforCte(serie_Decreciente,"Deformacion Decreciente desde M.Pr")

serie_RedPases1_2= calculoSerieDecrConRedDada1ero2doPase(do,df,pases,porc_red_pase1,porc_red_pase2,porc_red_ult_pase)
imprimir_serie_deforCte(serie_RedPases1_2,"Probando serie con reduccion establecida en pases 1 y 2")
graficar_serie(serie_RedPases1_2,pases)

'''
fe=0.20
while fe<0.31:
    np = round((( -2 * m.log(df/di))/ fe),0)
    k_df_di =  m.pow(df/di,1/np)
    k_di_df =  m.pow(di/df,1/np)# K= Factor de reduccion
    prp = (1-m.pow(k_df_di,2))*100 
    print(f"Numero pases : {np:.2f} %RedPase : {prp:.2f} K, df a di : {k_df_di:.3f} k,  di a df : {k_di_df:.3f}  para fe: {fe:.2f}" )
    fe+=0.01

''CALCULO DE SERIE CON REDUCCION CONSTANTE'''

'''
ϵt = 2 * ln (Do/Df)      # Deformacion total o puede ser por pase
                            𝜖𝑡= 2 ln 𝐷o/𝐷𝑓
'''



'''CALCULO DE PORCENTAJE DE REDUCCION POR PASE '''

''' Calculamos el numero de pasos :
        np = ( 2 x ln(df/di)/ 0.26),
            np : Numero de pasos.
            ln : Logararitmo neperiano ( logaritmo base e) 
            df : diametro final
            di : diametro inicial 
            0.26 : factor empirico.
    el factor de reduccion por paso: K = (df/di)^(1/np)
        K: Es el factor de reducción por paso.
        (df/di): Es la relación entre el diámetro final y el diámetro inicial.
        (1/np): Es el inverso del número de pasos.
        Significado: Esta fórmula calcula el factor de reducción que debe aplicarse en cada paso para lograr una reducción uniforme del diámetro.
    y reduccion promedio por pase : prp = ( k^2 -1)*100 , donde prp es el porcentaje de reduccion por pase 
    prp: Representa el porcentaje de reducción promedio por paso.
        K^2: Es el factor de reducción al cuadrado.
        Significado: Esta fórmula calcula el porcentaje de reducción de área promedio que se produce en cada paso del proceso de trefilado.
        
    Factor Empirico:
    El factor empírico de 0.26 en la fórmula del número de pasos (np) es un valor que se utiliza para estimar el número de pasos necesarios 
    en un proceso de trefilado. Sin embargo, este valor no es una constante universal y puede variar significativamente dependiendo de varios 
    factores.

    Factores que Influyen en el Factor Empírico:
    Material del Alambre: Las propiedades mecánicas del material, como su ductilidad, resistencia a la tracción y endurecimiento por deformación,
    influyen en el factor empírico.
    Materiales más dúctiles pueden tolerar mayores reducciones de área por paso, lo que puede resultar en un factor empírico menor.
    Lubricación: Una lubricación adecuada reduce la fricción entre el alambre y el dado, lo que permite mayores reducciones de área por paso.
    La calidad y el tipo de lubricante utilizado pueden afectar significativamente el factor empírico.
    Geometría del Dado: El ángulo de entrada y el ángulo de reducción del dado influyen en la deformación del alambre y la fuerza de trefilado.
    La geometría del dado puede afectar la eficiencia del proceso y, por lo tanto, el factor empírico.
    Velocidad de Trefilado: La velocidad a la que se estira el alambre puede afectar la temperatura y la deformación del material.
    Las altas velocidades de trefilado pueden generar calor, lo que puede afectar las propiedades del material y el factor empírico.
    Condiciones del Proceso: Otros factores, como la temperatura ambiente, la tensión de trefilado y la calidad del alambre inicial, también pueden influir 
    en el factor empírico.
    
    Valores Típicos para Diversos Materiales:
    Es difícil proporcionar valores exactos para el factor empírico, ya que depende de las condiciones específicas del proceso. Sin embargo, puedo proporcionar
    algunas pautas generales:
    
    Acero Bajo Carbono: Generalmente, el acero bajo carbono es muy dúctil y puede tolerar mayores reducciones de área por paso.
    El factor empírico puede variar entre 0.2 y 0.3.

    Acero Medio y Alto Carbono: Estos aceros son menos dúctiles que el acero bajo carbono y requieren reducciones de área por paso más pequeñas.
    El factor empírico puede variar entre 0.25 y 0.35.

    Cobre y Latón:
    El cobre y el latón son materiales muy dúctiles y pueden tolerar grandes reducciones de área por paso.
    El factor empírico puede variar entre 0.15 y 0.25.
    
    Aluminio:
    El aluminio es un material dúctil, pero su endurecimiento por deformación puede limitar las reducciones de área por paso.
    El factor empírico puede variar entre 0.2 y 0.3.
    
    Recomendaciones:
    Es importante realizar pruebas experimentales para determinar el factor empírico óptimo para un material y un proceso específicos.
    Se recomienda consultar las normas y las mejores prácticas de la industria para obtener información adicional sobre los factores empíricos 
    en el trefilado de alambre.    
        
'''