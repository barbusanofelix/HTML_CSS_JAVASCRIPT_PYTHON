class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_info(self):
        print(f"Libro: {self.titulo} - Autor: {self.autor}")

# Crear instancia
libro1 = Libro("1984", "George Orwell")

# Usar self implícitamente
libro1.mostrar_info()  # Output: "Libro: 1984 - Autor: George Orwell"