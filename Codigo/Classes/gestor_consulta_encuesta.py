import sys
from datetime import date, datetime
from llamada import Llamada
from encuesta import Encuesta

sys.path.append("../Codigo")
from Support.funciones_soporte import from_string_to_date


class GestorConsultaEncuesta:
    # def __init__(self, fecha_inicio_periodo: date, fecha_fin_periodo: date, llamada_seleccionada: llamada.Llamada,
    #               tipo_salida_consulta_seleccionada: str):
    def __init__(self):
        self.__fecha_inicio_periodo = None
        self.__fecha_fin_periodo = None
        self.__llamada_seleccionada = None
        self.__tipo_salida_consulta_seleccionada = None

        self.__llamadas = []
        self.__encuestas = []

    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter fecha_inicio_periodo
    @property
    def fecha_inicio_periodo(self):
        # Executes this code when object.att
        return self.__fecha_inicio_periodo

    # Setter fecha_inicio_periodo
    @fecha_inicio_periodo.setter
    def fecha_inicio_periodo(self, value):
        # Executes this code when object.att = value
        self.__fecha_inicio_periodo = value
    
    
    # Getter fecha_fin_periodo
    @property
    def fecha_fin_periodo(self):
        # Executes this code when object.att
        return self.__fecha_fin_periodo

    # Setter fecha_fin_periodo
    @fecha_fin_periodo.setter
    def fecha_fin_periodo(self, value):
        # Executes this code when object.att = value
        self.__fecha_fin_periodo = value

    # Getter llamada_seleccionada
    @property
    def llamada_seleccionada(self):
        # Executes this code when object.att
        return self.__llamada_seleccionada

    # Setter llamada_seleccionada
    @llamada_seleccionada.setter
    def llamada_seleccionada(self, value):
        # Executes this code when object.att = value
        self.__llamada_seleccionada = value
    
    # Getter tipo_salida_consulta_seleccionada
    @property
    def tipo_salida_consulta_seleccionada(self):
        # Executes this code when object.att
        return self.__tipo_salida_consulta_seleccionada

    # Setter tipo_salida_consulta_seleccionada
    @tipo_salida_consulta_seleccionada.setter
    def tipo_salida_consulta_seleccionada(self, value):
        # Executes this code when object.att = value
        self.__tipo_salida_consulta_seleccionada = value

    # Getter llamadas
    @property
    def llamadas(self):
        # Executes this code when object.att
        return self.__llamadas

    # Add llamada
    def add_llamada(self, nueva_llamada: Llamada):
        # Executes this code when object.att = value
        self.__llamadas.append(nueva_llamada)
    
    # Getter llamadas
    @property
    def encuestas(self):
        # Executes this code when object.att
        return self.__encuestas

    # Add encuesta
    def add_encuesta(self, nueva_encuesta: Encuesta):
        # Executes this code when object.att = value
        self.__encuestas.append(nueva_encuesta)
    



    # Metodos de ejecucion de CU

    # Mensaje 8
    def buscar_llamadas_en_periodo(self):
        """
        Filtra con el atributo de todas las llamadas

        # ver si fechas del periodo van como atributo del gestor, o como parametro del metodo
        # fecha_inicio_periodo_date = from_string_to_date(fecha_inicio_periodo)
        # fecha_fin_periodo_date = from_string_to_date(fecha_fin_periodo)
        # Las fechas del periodo son atributos del objeto de gestor
        """
        
        llamadas_en_periodo_con_respuesta = []
        for llamada in self.llamadas:
            # Ejecutamos dos metodos de llamada y le pasamos por parametro los atributos de gestor (fechas periodo: formato date)
            if llamada.es_de_periodo(self.fecha_inicio_periodo, self.fecha_fin_periodo) and llamada.tiene_respuesta_encuesta():
                # print("llamada en periodo y con respuesta")
                llamadas_en_periodo_con_respuesta.append(llamada)

        return llamadas_en_periodo_con_respuesta
    


    # Mensaje 16
    def buscar_datos_llamada(self):
        # Mensaje 17
        nombre_cliente_llamada = self.llamada_seleccionada.get_nombre_de_cliente()
        # Mensaje 19
        nombre_estado_actual = self.buscar_ultimo_estado_llamada()
        # Mensaje 23.2
        duracion_llamada = self.llamada_seleccionada.duracion
        # Mensaje 24
        datos_encuestas_por_respuesta_cliente = self.buscar_encuesta_de_respuesta()

        return {"cliente": nombre_cliente_llamada,
                "estado_actual": nombre_estado_actual,
                "duracion": duracion_llamada,
                "datos_encuesta": datos_encuestas_por_respuesta_cliente}

    # Mensaje 19
    def buscar_ultimo_estado_llamada(self):
        # Mensaje 20
        ultimo_estado_llamada = self.llamada_seleccionada.buscar_ultimo_estado()
        return ultimo_estado_llamada


    # Mensaje 24
    def buscar_encuesta_de_respuesta(self):
        """
        Toma el atributo de llamada seleccionada y busca toda la informacion necesaria que se describe en el CU
        """
        todos_datos_respuestas_de_llamada = []
        # Buscar las respuestas del cliente
        # Mensaje 25
        for respuesta_cliente in self.llamada_seleccionada.respuestas_de_encuesta:  
            # Mensajes 26 y 27
            descripcion_respuesta_cliente = respuesta_cliente.get_descripcion_rta()

            # Mensaje 28    -> Buscar datos de la encuesta de llamada segun la respuesta del cliente
            datos_respuesta_de_llamada = self.buscar_datos_encuesta_llamada(descripcion_respuesta_cliente)
            if datos_respuesta_de_llamada:  # Si no es una lista vacia
                todos_datos_respuestas_de_llamada.extend(datos_respuesta_de_llamada)  # Muy importante mergear las listas y no agregar otra lista dentro de otra
        return todos_datos_respuestas_de_llamada
            
    

    # Mensaje 28
    def buscar_datos_encuesta_llamada(self, respuesta_cliente):
        """
        Busca los datos de la repuesta, su pregunta, su encuesta
        """
        datos_respuesta_de_llamada = []
        for encuesta in self.encuestas:
            # Mensaje 29
            datos_respuesta = encuesta.es_tu_respuesta(respuesta_cliente)
            # Si es respuesta posible de la encuesta
            if datos_respuesta != False:
                datos_respuesta_de_llamada.append(datos_respuesta)
        return datos_respuesta_de_llamada








"""
# ---------------
# -  Pruebilla  -
# ---------------

# CADA INSTANCIA DE CADA CLASE DEBE SER CREADA EN EL ARCHIVO DE LA CLASE CORRESPONDIENTE, 
# ASI CUANDO IMPORTEMOS CADA MODULO, SE IMPORTA LA CLASE Y LOS OBJETOS, EN ESTE CASO DE PRUEBA

# import Estado.cambio_estado
from llamada import Llamada
from cliente import Cliente
from Estado.cambio_estado import CambioEstado
from Estado.estado import Estado
from respuesta_de_cliente import RespuestaDeCliente
from respuesta_posible import RespuestaPosible

r_posible = RespuestaPosible("Correcto", "12")

r_cliente = RespuestaDeCliente(datetime(2001, 4, 12, 18, 34, 20), r_posible)

estado_iniciado = Estado("Iniciado")
cambio_estado_1 = CambioEstado(datetime(2001, 4, 12, 18, 14, 20), estado_iniciado) 
cambio_estado_2 = CambioEstado(datetime(2012, 4, 12, 18, 14, 20), estado_iniciado) 

# cambio_estado_3 = CambioEstado(datetime(2022, 4, 12, 18, 14, 20), estado_iniciado) 

cliente1 = Cliente("23453432", "Humberto Primo", "3513433777")

llamada1 = Llamada("Flaquito 1", "Llama profesional", 3.3, True, "Completada", cliente1, cambio_estado_1)
llamada1.add_respuesta_encuesta(r_cliente)

llamada2 = Llamada("Furroberto", "Llama a Motel", 6.7, True, "Completada", cliente1, cambio_estado_2)


fecha_inicio_periodo = date(2000, 4, 21)
fecha_fin_periodo = date(2009, 4, 21)

gestor = GestorConsultaEncuesta()
gestor.fecha_inicio_periodo = fecha_inicio_periodo
gestor.fecha_fin_periodo = fecha_fin_periodo
gestor.llamadas.append(llamada1)
gestor.llamadas.append(llamada2)

filtro = gestor.buscar_llamadas_en_periodo()
print(filtro)
for llamada_found in filtro:
    print(llamada_found.descripcion_operador)

"""

