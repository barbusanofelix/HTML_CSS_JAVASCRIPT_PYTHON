
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

    
def calculoSerieDecrConRedDada1ero2doPase(do,df,porc_red1, porc_red2, porc_red_ult_pase):                       # calculo Serie Decrec con reduccion Dada en 1ero, 2do pase 
    serieDecRed1_2=[]                                              # Serie decreciente desde 3er a ultimo pase
    serieDecRed1_2=[(do,0,0)]
    
    defor_p1=deforUnPase(porc_red1)
    print("Deformacion pase 1 para red=20%", defor_p1)
    d1=df_vs_do_defor(do,defor_p1)
    print("d1 =", d1)
    serieDecRed1_2.append((d1,porc_red1,defor_p1))                  # No olvidar los parentisis de la Tupla.
    
    defor_p2=deforUnPase(porc_red2)
    d2=df_vs_do_defor(d1,defor_p2)
    serieDecRed1_2.append((d2,porc_red2,defor_p2))
    
    # Ahora tengo que calcular una serie con reduccion decreciente donde el Do = d2 y los pasos serian pasos-2
    # Luego, tengo que añadir la serie obtenida desde el paso 1 hasta el paso final empezando desde la posicion 3 (Ya tengo añadio 0,1 y 2)
    # Primero calculo la deformacion de los pases.
    
    e_individual_repartida=deforEi(d2,df,pases-2,24)
    
    e_total=deforEntrePases(d2,df)
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
     
             
do=6.35
df=2.032
porc_red_pase1=20
porc_red_pase2=25
porc_red_ult_pase=16   
pases=8


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

serie_RedPases1_2= calculoSerieDecrConRedDada1ero2doPase(do,df,20,25,24)
imprimir_serie_deforCte(serie_RedPases1_2,"Probando serie con reduccion establecida en pases 1 y 2")

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