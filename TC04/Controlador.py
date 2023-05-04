from Modelo import Biblioteca, Libro, Prestamo

libros = []
prestamos = []

libro1 = Libro(1,"Drácula", "Bram Stoker", "1897", "Alma","Español")
libros.append(libro1)

if (libro1.getLibro(1,libros) == True):
    print("Man")

