# Pass simpemente no hace nada, es una operación nula. Se puede usar cuando se requiere una declaración sintáctica pero no se necesita ninguna acción. Por ejemplo:
# Un ejemplo util de pass podria ser cuando se quiere hacer una declaración de un bloque de código que no se ha implementado todavía, pero se quiere que el código se ejecute sin errores.

x = 5

while x > 0:
    x = x -1
    if x == 3:
        pass # No hacer nada cuando x es igual a 3
    else:
        print(x)