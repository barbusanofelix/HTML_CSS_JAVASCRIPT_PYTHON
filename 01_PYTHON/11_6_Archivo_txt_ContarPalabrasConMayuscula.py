
# Abre un archivo txt
# Asigne al mismo a la variable text y busca las mayusculas en cada caracter 

archivo = r"E:\Python\Detectar Mayusculas.txt"  # Reemplaza con tu ruta y nombre de archivo
with open(archivo) as fh:
    numMayus = 0
    text = fh.read()
for character in text:
    if character.isupper():
        numMayus += 1
print(f"Mayusculas en archivo {archivo}:",numMayus )      

'''
EXPLICACION DEL CODIGO
Análisis del código:
with open(archivo) as fh:
Esta línea intenta abrir un archivo cuyo nombre está almacenado en la variable archivo.
with open(...) asegura que el archivo se cierre automáticamente después de que se termine de trabajar con él, 
incluso si ocurren errores.
as fh asigna el objeto de archivo abierto a la variable fh (file handle).
count = 0: Inicializa una variable count en 0 para almacenar el número de letras mayúsculas encontradas.
text = fh.read():
Lee todo el contenido del archivo y lo almacena en la variable text como una cadena.

for character in text:
Itera sobre cada carácter en la cadena text.

if character.isupper():
Verifica si el carácter actual es una letra mayúscula.
count += 1:
Si el carácter es una letra mayúscula, incrementa el contador count en 1.

Integrar la ruta del archivo:
Para integrar la ruta del archivo, simplemente asigna la ruta completa a la variable archivo antes de abrir
el archivo. Recuerda usar r para las rutas "raw".

archivo = r"E:\Python\Detectar Mayusculas.txt":
Se asigna la ruta completa del archivo a la variable archivo.
Se utiliza r antes de la cadena para crear una "raw string", lo que evita problemas con caracteres de escape 
en la ruta.

'''