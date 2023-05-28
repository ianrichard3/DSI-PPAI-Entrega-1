import respuesta_posible

class Pregunta:
    def __init__(self, pregunta: str):
        # Atributos propios
        self.__pregunta = pregunta

        # Atributos referencia
        self.__respuestas = []

    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter pregunta
    @property
    def pregunta(self):
        # Executes this code when w1.name
        return self.__pregunta

    # Setter pregunta
    @pregunta.setter
    def pregunta(self, value):
        # Executes this code when w1.name = something
        if len(value) > 15:
            raise Exception("Flayaste, muy largo")
        else:
            self.__pregunta = value

    # Getter respuestas
    @property
    def respuestas(self):
        # Executes this code when w1.name
        return self.__respuestas

    # Add respuesta posible
    def add_respuesta(self, respuesta: respuesta_posible.RespuestaPosible):
        self.__respuestas.append(respuesta)

    
    # Metodos de CU

    # Mensaje 31.a
    def listar_respuestas_posibles(self):
        """
        Busca en todas sus respuestas posibles, las descripciones
        """
        # Mensaje 31.b
        descripciones_respuestas = [rta.descripcion for rta in self.respuestas]
        # for rta in self.respuestas:
        #     descripciones_respuestas.append(rta.descripcion)  # mensaje 31.b
        return descripciones_respuestas

