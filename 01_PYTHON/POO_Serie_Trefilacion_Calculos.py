
import math as m


def deforEntrePases(do,df):                 #* Calcula la deformacion Total entre pases ( Puede ser entre cualquier tramo )
    return 2*m.log(do/df)

def PorcRedConDiam(do,df):
    return (1-pow(df/do,2))*100             #* Calcula el Porcentaje Reduccion en base a los Diametros ( Porc= Porcentaje, Red=Reduccion ConDiam = Con diametros)

def PorcRedConDefor(deformacion):           #* %Red =(1-EXP(-Et))*100 , Et= Defomacion ( deformacionEntrePases(do,df): )
    return (1-pow(m.e,-deformacion))*100  

def df_vs_do_defor(do,deformacion):         #* Calcula el diametro siguiente ( De arriba hacia abajo, descendiente ) para la deformacion  Df=Do*EXP(-Et/2) ...recuerda que EXP es "e" elevado a -Et/2
    return do*pow(m.e,-deformacion/2)

def do_vs_df_defor(df,deformacion):         #* Calcula el diametro previo ( de abajo hacia arriba  )dando el diametro final y la deformacion        
    return df/(pow(m.e,deformacion))

def deforPorPase(do,df,pases):              #* Calcula la deformacion promedio entre pases....Puede ser toda la serie o entre cualquier numero.
    deforEntreDoDf= deforEntrePases(do,df)  #! Esta deformacion se puede usar para el calcuo de serie con deformacion constante.
    return deforEntreDoDf/pases
    

def calculoSerieDeforCte(do, df, pases):
    serie = []
    serie.append(do)
    deforCte = deforPorPase(do, df, pases)
    for i in range(1, pases + 1):
        serie.append(round(df_vs_do_defor(serie[i - 1], deforCte),3))  # Truncar a 2 decimales
    return serie
    
         
        
    
    
    
    
do=6.35
df=2.032   
pases=8
deformacionTotal = deforEntrePases(do,df)
print(f"Do : {do:.2f}  Df : {df:.2f}  Deformacion : {deforEntrePases(do,df):.4f} %Red_diam {PorcRedConDiam(do,df):.2f} %Red_Def :{PorcRedConDefor(deformacionTotal):.2f}")
print(f"Df vs Deformacion : {df_vs_do_defor(6.35,2.2789):.4f}")
print(f"Deformacion/pase : {deforPorPase(do, df, pases):.4f}")

serie= calculoSerieDeforCte(do,df,pases)
print(serie)


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