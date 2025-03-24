
import math as m  #? Importamos el modulo math y le colocamos el alias de m

#?Vemos todo lo que nos ofrece math
print(dir(m))

#* Genera la salida:
'''
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 
'acos'   , 'acosh', 'asin' , 'asinh', 'atan'     , 'atan2'   , 'atanh', 'cbrt', 'ceil'     , 'comb'   , 'copysign' , 'cos'   , 'cosh' , 'degrees', 
'dist'   , 'e'    , 'erf'  , 'erfc' , 'exp'      , 'exp2'    , 'expm1', 'fabs', 'factorial', 'floor'  , 'fma'      , 'fmod'  , 'frexp', 'fsum', 
'gamma'  , 'gcd'  , 'hypot', 'inf'  , 'isclose'  , 'isfinite', 'isinf', 'isnan', 'isqrt'   , 'lcm'    , 'ldexp'    , 'lgamma', 'log'  , 'log10', 
'log1p'  , 'log2' , 'modf' , 'nan'  , 'nextafter', 'perm'    , 'pi'   , 'pow'  , 'prod'    , 'radians', 'remainder', 'sin'   , 'sinh' , 'sqrt', 
'sumprod', 'tan' , 'tanh'  , 'tau'  , 'trunc'    , 'ulp']

Entre otros tenemos arc coseno, arco tangente, coseno, seno, grados, numero e, exponencial, factorial, redondeo al minimo ( floor),
logaritmo base 10, logaritmo neperiano, boolean si es infinito, numero pi, potencia ( pow) radianes, raiz cuadrada ( sqrt ), truncar... 

'''
print(f"\n{'Funcion':<25} {'Resultado':<20}{'Valor Esperado':<20}")
print(f"{'Numero pi':<25} : {m.pi:<20}{'3.141516...':<20}")
print(f"{'Numero e':<25} : {m.e:<20}{'2,71.....':<20} ")
print(f"{'Suelo de pi':<25} : {m.floor(m.pi):<20} {'3':<20}")
print(f"{'Potencia 2 a 10':<25} : {m.pow(2,10):<20} {'1024':<20}")
print(f"{'Factorial de 5':<25} : {m.factorial(5):<20} {'120':<20}")
print(f"{'Raiz cuadrada de 36':<25} : {m.sqrt(36):<20} {'120':<20}")
print(f"{'Log 10 de 1000 ':<25} : {m.log10(1000):<20} {'3':<20}")
print(f"{'Ln de 1000 ':<25} : {m.log(1000):<20} {'6,907755':<20}")