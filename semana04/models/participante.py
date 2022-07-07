from email.policy import default
from config import conexion
from sqlalchemy import Column, types

class Participante(conexion.Model):
    # ahora esta clase tendra un comportamiento en forma de una tabla en la bd (todos los atributos que declara que sea propios de la bd se creara como columnas)
    # conexion.Column() = Column
    # Documentacion > https://docs.sqlalchemy.org/en/14/core/metadata.html?highlight=column#sqlalchemy.schema.Column.__init__
    # si no se pone el parametro 'name' este sera el mismo que el nombre del atributo 
    # cuando usamos un tipode de dato en mayusculas este tipo de datos es especifico para un determinado motor de base de datos

    id = Column(type_= types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.String(50), nullable=False)
    apellido = Column(type_=types.String(50), nullable=False)
    telefono = Column(type_=types.String(10))
    password = Column(type_=types.Text, nullable=False)
    zona = Column(type_=types.Enum('SUPER_VIP', 'VIP', 'GENERAL'), 
                  default = 'GENERAL', nullable=False)
    comentario = Column(type_=types.Text)
    correo = Column(type_=types.String(45), nullable=False)

    # se modificara el nombre dde la tabla a nivel de base de datos para que no se llame igual que la clase (en singular y con la primera en mayuscula)
    __tablename__ = 'pasticipantes' 