

# -------------
# - Pruebilla -
# -------------

# CADA INSTANCIA DE CADA CLASE DEBE SER CREADA EN EL ARCHIVO DE LA CLASE CORRESPONDIENTE, 
# ASI CUANDO IMPORTEMOS CADA MODULO, SE IMPORTA LA CLASE Y LOS OBJETOS, EN ESTE CASO DE PRUEBA


from llamada import Llamada
from cliente import Cliente
from Estado.cambio_estado import CambioEstado
from Estado.estado import Estado
from respuesta_de_cliente import RespuestaDeCliente
from respuesta_posible import RespuestaPosible
from encuesta import Encuesta
from pregunta import Pregunta
from gestor_consulta_encuesta import GestorConsultaEncuesta

from datetime import date, datetime
import sys


sys.path.append("../Codigo")
from Support.funciones_soporte import from_string_to_date


#  //// TEST mensajes 8-11
""" 
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

for llamada_found in gestor.buscar_llamadas_en_periodo():
    print(llamada_found.descripcion_operador)
"""


#  //// Test mensajes 24-33

# Ejemplos encuestas

fecha_fin_vigencia = date(2010, 4, 21)

# pregunta 1
pregunta1_encuesta1 = Pregunta("Te gusto?")
rta1_pregunta1_encuesta1 = RespuestaPosible("Si", "Si")
rta2_pregunta1_encuesta1 = RespuestaPosible("No", "No")
pregunta1_encuesta1.add_respuesta(rta1_pregunta1_encuesta1)
pregunta1_encuesta1.add_respuesta(rta2_pregunta1_encuesta1)

# pregunta 2

pregunta2_encuesta1 = Pregunta("Reseña de llamada:")
rta1_pregunta2_encuesta1 = RespuestaPosible("Buena", "Buena")
rta2_pregunta2_encuesta1 = RespuestaPosible("Mala", "Mala")
rta3_pregunta2_encuesta1 = RespuestaPosible("Muy buena", "Muy buena")
rta4_pregunta2_encuesta1 = RespuestaPosible("Muy mala", "Muy mala")
pregunta2_encuesta1.add_respuesta(rta1_pregunta2_encuesta1)
pregunta2_encuesta1.add_respuesta(rta2_pregunta2_encuesta1)
pregunta2_encuesta1.add_respuesta(rta3_pregunta2_encuesta1)
pregunta2_encuesta1.add_respuesta(rta4_pregunta2_encuesta1)

# pregunta 3 (p 1 encuesta 2)
pregunta1_encuesta2 = Pregunta("Como andas amigo")
rta1_pregunta3_encuesta1 = RespuestaPosible("Bien", "Bien")
rta2_pregunta3_encuesta1 = RespuestaPosible("Mal", "Mal")
pregunta1_encuesta2.add_respuesta(rta1_pregunta3_encuesta1)
pregunta1_encuesta2.add_respuesta(rta2_pregunta3_encuesta1)





encuesta2 = Encuesta("Encuesta numero 1", fecha_fin_vigencia)
encuesta2.add_pregunta(pregunta1_encuesta1)
encuesta2.add_pregunta(pregunta2_encuesta1)

encuesta1 = Encuesta("Encuesta numero 2", fecha_fin_vigencia)
encuesta1.add_pregunta(pregunta1_encuesta2)








# datos llamada
cliente1 = Cliente("23453432", "Humberto Primo", "3513433777")
estado_iniciado = Estado("Iniciado")
cambio_estado_1 = CambioEstado(datetime(2001, 4, 12, 18, 14, 20), estado_iniciado) 
llamada1 = Llamada("Flaquito 1", "Llama profesional", 3.3, True, "Completada", cliente1, cambio_estado_1)
r_cliente1 = RespuestaDeCliente(datetime(2001, 4, 12, 18, 34, 20), rta1_pregunta2_encuesta1)
r_cliente2 = RespuestaDeCliente(datetime(2001, 4, 12, 18, 34, 20), rta1_pregunta3_encuesta1)
r_cliente3 = RespuestaDeCliente(datetime(2001, 4, 12, 18, 34, 20), rta4_pregunta2_encuesta1)


llamada1.add_respuesta_encuesta(r_cliente1)
llamada1.add_respuesta_encuesta(r_cliente2)
llamada1.add_respuesta_encuesta(r_cliente3)

# Creacion Gestor

gestor = GestorConsultaEncuesta()
gestor.llamada_seleccionada = llamada1
gestor.add_encuesta(encuesta1)
gestor.add_encuesta(encuesta2)

datos_encuestas = gestor.buscar_encuesta_de_respuesta()

# print(datos_encuestas)
for datos_encuesta in datos_encuestas:
    # print(datos_encuesta)
    preg = datos_encuesta.get("pregunta")
    rta = datos_encuesta.get("respuesta")
    enc = datos_encuesta.get("encuesta")
    print(f"Pregunta: '{preg}'  |  Respuesta: '{rta}'  |  Encuesta:  '{enc}'")