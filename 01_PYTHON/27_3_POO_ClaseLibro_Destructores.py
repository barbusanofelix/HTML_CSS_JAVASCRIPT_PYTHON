

'''
clase para trabajar con libros.
EL DESTRUCTOR ES SIMPLEMENTE BORRAR CUALQUIER OBJETO QUE SE HAYA INSTANCIADO DE LA CLASE Book
Y PARA ELLO NO HACE FALTA CREAR LA FUNCION def __del__(self):
FUNCIONA CON SOLO:
    del libro    [ Siendo libro un objeto instanciado de la clase]
'''

class Book():

    def __init__(self, title, author = "",electronic = False):
        self.title = title
        self.author = author
        self.is_electronic = electronic


#! PARA EL BORRADO DE UN OBJETO DE LA CLASE EN TEORIA SE USA, por ejemplo  del libro
#! Y FUNCIONA SIN USAR LA CLASE SIGUIENTE....SIMPLEMENTE del libro
  #*  def __del__(self):
  #*     pass

libro=Book("Isla Mayor","",True)
libro2=Book("Isla Menor","",False)

print(libro.title)
print(libro.is_electronic)


print(libro.title)
print("Tipo de libro", type(libro))
del libro
print(libro2.title)
try:
    print(libro.title)
except Exception as e:
    print(e) 
    print("Esta claro que hubo un error")   
    print(libro2.title)
del libro2

try:
    print(libro2.title)
except Exception as e:
    print(e) 
    print("Esta claro que hubo otro error")  