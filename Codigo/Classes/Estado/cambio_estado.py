from Estado.estado import Estado
from datetime import datetime, date


class CambioEstado:
    def __init__(self, fecha_hora_inicio: datetime, estado: Estado):
        # Atributo propio
        self.__fecha_hora_inicio = fecha_hora_inicio

        # Atributo referencia
        self.__estado = estado


    # Getter fecha_hora_inicio
    @property
    def fecha_hora_inicio(self):
        # Executes this code when object.att
        return self.__fecha_hora_inicio 

    # Setter fecha_hora_inicio
    @fecha_hora_inicio.setter
    def fecha_hora_inicio(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__fecha_hora_inicio = value

    # Getter estado
    @property
    def estado(self):
        # Executes this code when object.att
        return self.__estado
    
    # Setter estado
    @estado.setter
    def estado(self, value):
        # Executes this code when object.att
        self.__estado = value