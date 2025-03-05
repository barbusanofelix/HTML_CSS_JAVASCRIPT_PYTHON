import docx

def contar_mayusculas_docx(nombre_archivo):
    try:
        doc = docx.Document(nombre_archivo)
        contenido = ""
        for parrafo in doc.paragraphs:
            contenido += parrafo.text
        contador = 0
        for caracter in contenido:
            if caracter.isupper():
                contador += 1
        return contador
    except FileNotFoundError:
        return "El archivo no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"

nombre_archivo = r"E:\Python\Detectar Mayusculas.docx"
mayusculas = contar_mayusculas_docx(nombre_archivo)
print(f"Número de mayúsculas en el archivo {nombre_archivo}: {mayusculas}")