import datetime 

class Biblioteca:
    nombre = ""
    direccion = ""
    horario = ""
    correo = ""
    telefono = 0
    
    def __init__(self, nombre, direccion, horario, correo, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.horario = horario
        self.correo =correo
        self.telefono = 0

#manolo = Biblioteca("Bibliotec", "Cartago", "8am a 9 pm", "bibliotec.itcr.ac.cr", 24588934)

class Libro:
    codigoLibro = 0
    nombre = ""
    autor = ""
    fechaPublicado = ""
    editorial = ""
    idioma = ""
    
    def __init__(self, codigoLibro, nombre, autor, fechaPublicado, editorial, idioma):
        self.codigoLibro = codigoLibro
        self.nombre = nombre
        self.autor = autor
        self.fechaPublicado = fechaPublicado
        self.editorial = editorial
        self.idioma = idioma

    def getLibro(self,codigo,libros):
        i = 0
        if (len(libros) != 0):
            while i < len(libros):
                if (libros[i].codigoLibro == codigo):
                    return True
                    break
                i = i+1
        else:
            return False
#librillo = Libro(1,"Draculin","Mario","1934","Paquita", "Español")

class Prestamo:
    idTrabajador = 0
    carnetEst = 0
    fechaPrest = ""
    fechaDev = ""
    codLibro = 0
    sumar = 0

    def setPrest(self,carnet,idB,codLibro):
        self.carnetEst = carnet
        self.idTrabajador = idB
        self.codLibro = codLibro
        self.fechaPrest = datetime.date.today()
        self.sumar = datetime.timedelta(days=2)
        self.fechaDev =  self.fechaPrest + self.sumar

    def getPrest(self, carnet, codLibro, prestamos):
        i = 0
        while(i < len(prestamos)):
            if(prestamos[i].canetEst == carnet and prestamos[i].codLibro == codLibro):
                return True
                break
            else:
                return False


#class RegistroDePrestamos:
#class Usuario:
#class Bibliotecario:
#class Estudiante: