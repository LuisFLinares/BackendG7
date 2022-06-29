# En python el polimorfismo es la definicion del mismo metodo en diferentes clases pero con un comportamiento diferente 
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def info(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido
        }

class Alumno(Usuario):
    def __init__(self, Nombre, apellido2, año, seccion):
        self.año = año
        self.seccion = seccion
        # (super) es un metodo que sirve para utilizar los metodos y atributos de la clase o clases que estamos heredando
        # y ya con esto he llamado a mi constructor pero del padre
        super().__init__(nombre= Nombre, apellido = apellido2)
    
    def info(self):
        infoUsuario = super().info()
        data= {
            'nombre': self.nombre,
            'año': self.año,
        }
        # En python para hacer destructuracion de un diccinario se realiza de la siguiente manera
        return{**data, **infoUsuario}
alumnoEduardo = Alumno('Eduardo', 'de Rivero', 'Sexto', 'A')

usuarioRaul = Usuario('Raul','Mendoza')

informacion = alumnoEduardo.info()
print(informacion)
print(usuarioRaul.info())

