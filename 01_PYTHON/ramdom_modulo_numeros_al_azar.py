
'''
Alguna de las funciones mas comunes del modulo random

'''

import random as r

print(dir(r))

#! La salida o el dir de ramdom es:
'''
['BPF'      , 'LOG4'        , 'NV_MAGICCONST'   , 'RECIP_BPF'       , 'Random'      , 'SG_MAGICCONST'       , 'SystemRandom'    , 'TWOPI'       , 
'_ONE'      , '_Sequence'   , '__all__'         , '__builtins__'    , '__cached__'  , '__doc__'             , '__file__'        , '__loader__',
'__name__'  , '__package__' , '__spec__'        , '_accumulate'     , '_acos'       , '_bisect'             , '_ceil'           , '_cos'      , 
'_e', '_exp', '_fabs'       , '_floor'          , '_index'          , '_inst'       , '_isfinite'           , '_lgamma'         , '_log'        ,
'_log2'     , '_os'         , '_parse_args'     , '_pi'             , '_random'     , '_repeat'             , '_sha512'         , '_sin'        ,
'_sqrt'     , '_test'       , '_test_generator' , '_urandom'        , 'betavariate' , 'binomialvariate'     , 'choice'          , 'choices'     ,
'expovariate','gammavariate', 'gauss'           , 'getrandbits'     , 'getstate'    , 'lognormvariate'      , 'main'            , 'normalvariate',
'paretovariate', 'randbytes', 'randint'         , 'random'          , 'randrange'   , 'sample'              , 'seed'            , 'setstate'    ,
'shuffle'   , 'triangular'  , 'uniform'         , 'vonmisesvariate' , 'weibullvariate']
'''

print(f"\n{'Funcion':<40}{'Resultado':<20}   {'Valor Esperado':<20}")
print(f"{'Numero aleaorio ( 0 - 1) ':<40}: {r.random():<20} {'Aleaorio entre 0 a 1':<20}")
print(f"{'Numero aleaorio, float [-10, 40] ':<40}: {r.uniform(-10,40):<20} {'Aleaorio en el rango inicado':<20}")
print(f"{'Numero aleaorio, int [-10, 40] ':<40}: {r.randint(-10,40):<20} {'Aleaorio en el rango inicado':<20}")
baraja = ["Corazón", "Diamante", "Trébol", "Pica"]
print(f"{'Baraja':<40}: {baraja}")
print(f"{'Elemento aleatorio':<40}: {r.choice(baraja)}")
r.shuffle(baraja)
print(f"{'Baraja mezclada':<40} {baraja}\n")

