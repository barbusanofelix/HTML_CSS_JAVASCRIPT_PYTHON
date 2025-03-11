'''
BUENA PRACTICA PARA LA CAPTURA DEL ERROR:
  Separar el IndexError y el TypeError 
'''

def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 7)             # El indice debe ser <=6 ( Python tiene 6 caracteres)
except IndexError as indErr:
    print(f'Error de índice: {indErr}')
except TypeError as tyErr:
    print(f'Error de tipo: {tyErr}')
except Exception as otroError:
    print(f'Otro tipo de error: {otroError}')    
print('Hemos salido del try-catch')

try:
    indexador('Python', 0)
except IndexError as indErr:
    print(f'Error de índice: {indErr}')
except TypeError as tyErr:
    print(f'Error de tipo: {tyErr}')
except Exception as otroError:
    print(f'Otro tipo de error: {otroError}')    
print('Hemos salido del try-catch')
