'''
La sentencia ‘assert’
Además de lanzar excepciones manualmente, es posible hacerlo condicionalmente. Para ello, Python
proporciona la sentencia assert que nos permite lanzar una excepción si se cumple una condición
determinada.
Es muy común utilizar la sentencia assert durante el proceso de depuración, para asegurarnos que se
cumplen ciertas condiciones previas.
La sintaxis de assert es la siguiente:

    assert(condición), ‘Mensaje de error’ 

Una NOTA IMPORTANTE sobre esta la sentencia assert:
su uso es muy útil para detectar errores en depuración, pero no se recomienda el uso de assert en producción.    
'''


a = 100
b = 0
assert(a > b), 'A tiene que ser mayor que B!' # Si se cumple no salta el error
print('Si se muestra esto es que no ha saltado el assert')
