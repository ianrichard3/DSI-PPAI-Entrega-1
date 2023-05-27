import cliente as cliente_class
import Estado.cambio_estado as cambio_estado
import respuesta_de_cliente
from datetime import date


class Llamada:
    def __init__(self, descripcion_operador: str, detalle_accion: str,
                 duracion: float, encuesta_enviada: bool, observacion_auditor: str, cliente: cliente_class.Cliente, primer_cambio_estado: cambio_estado.CambioEstado):
        # Validaciones
        assert duracion > 0.0, "La duracion debe ser mayor a cero"

        # Atributos propios

        self.__descripcion_operador = descripcion_operador
        self.__detalle_accion = detalle_accion
        self.__encuesta_enviada = encuesta_enviada
        self.__observacion_auditor = observacion_auditor
        self.__duracion = duracion

        # Atributos referencia
        self.__respuestas_de_encuesta = []
        self.__cambios_estado = [primer_cambio_estado]
        self.__cliente = cliente


    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter descripcion_operador
    @property
    def descripcion_operador(self):
        # Executes this code when object.att
        return self.__descripcion_operador

    # Setter descripcion_operador
    @descripcion_operador.setter
    def descripcion_operador(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__descripcion_operador = value

    # Getter detalle_accion
    @property
    def detalle_accion(self):
        # Executes this code when object.att
        return self.__detalle_accion


    # Setter detalle_accion
    @detalle_accion.setter
    def detalle_accion(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__detalle_accion = value


    # Getter encuesta_enviada
    @property
    def encuesta_enviada(self):
        # Executes this code when object.att
        return self.__encuesta_enviada

    # Setter encuesta_enviada
    @encuesta_enviada.setter
    def encuesta_enviada(self, value):
        # Executes this code when object.att = value
        self.__encuesta_enviada = value


    # Getter observacion_auditor
    @property
    def observacion_auditor(self):
        # Executes this code when object.att
        return self.__observacion_auditor

    # Setter observacion_auditor
    @observacion_auditor.setter
    def observacion_auditor(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__observacion_auditor = value

    # Getter duracion
    @property
    def duracion(self):
        # Executes this code when object.att
        return self.__duracion

    # Setter duracion
    @duracion.setter
    def duracion(self, value):
        # Executes this code when object.att = value
        if value < 0.0:
            raise Exception("No puede ser negativo")
        else:
            self.__duracion = value

    # Getter duracion
    @property
    def cliente(self):
        # Executes this code when object.att
        return self.__cliente

    # Setter duracion
    @cliente.setter
    def cliente(self, value):
        # Executes this code when object.att = value
        self.__cliente = value

    # Getter respuestas_de_encuesta
    @property
    def respuestas_de_encuesta(self):
        # Executes this code when object.att
        return self.__respuestas_de_encuesta
    
    # Add respuesta de encuesta
    def add_respuesta_encuesta(self, respuesta_encuesta: respuesta_de_cliente.RespuestaDeCliente):
        self.__respuestas_de_encuesta.append(respuesta_encuesta)

    # Getter cambio_estado
    @property
    def cambios_estado(self):
        # Executes this code when object.att
        return self.__cambios_estado
    
    # Add cambio de estado
    def add_cambio_estado(self, cambio_estado: cambio_estado.CambioEstado):
        self.__cambios_estado.append(cambio_estado)
            
    


    # Metodos de ejecucion de CU

    # mensaje 9
    def es_de_periodo(self, fecha_inicio_periodo: date, fecha_fin_periodo: date):
        primer_cambio_estado = self.cambios_estado[0]
        fecha_inicio_llamada = primer_cambio_estado.fecha_hora_inicio.date()
        if fecha_inicio_periodo < fecha_inicio_llamada < fecha_fin_periodo:
            print(f"Llamada en periodo!")
            return True
        return False
    
    # mensaje 10   - y el mensaje 11 con el len
    def tiene_respuesta_encuesta(self):
        # return len(self.respuestas_de_encuesta) > 0
        return self.respuestas_de_encuesta # Mensaje 11