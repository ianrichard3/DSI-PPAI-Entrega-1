import customtkinter as ctk
import tkinter as tk
import tkcalendar as tkc

import os
import sys



this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "...\\"))

# print(os.path.join(this_file_path))
# from Classes.GUI.Top_Level.llamada_seleccionada_top_level import LlamadaSeleccionadaTopLevel

from Classes.GUI.Top_Level.llamada_seleccionada_top_level import LlamadaSeleccionadaTopLevel
from Classes.GUI.Top_Level.message_box_top_level import MessageBoxTopLevel

# from gestor_consulta_encuesta import GestorConsultaEncuesta
from Support.funciones_soporte import from_string_to_date
from Support.funciones_soporte import from_call_dictionary_to_string

# from Support.funciones_soporte import from_call_string_get_call_object

# Constantes

FUENTE = "Helvetica"

llamadas_array = [
    "Llamada 1 | Ian Richard | Fecha 12/4/2022 | Hora 14:22",
    "Llamada 2 | Ian Rechard | Fecha 12/6/2022 | Hora 22:22",
    "Llamada 3 | Ian Rochard | Fecha 2/4/2022 | Hora 11:11",
    "Llamada 4 | Ian Ruchard | Fecha 11/4/2022 | Hora 14:22",
    "Llamada 5 | Ian Rachard | Fecha 31/3/2022 | Hora 14:13",

]

# Theme setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")






# class FrameDatosLlamadaSeleccionada(ctk.CTkScrollableFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # Aca van los widgets del frame de los datos
#         # De la llamada Seleccionada



class PantallaConsultarEncuesta(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("TESTEANDO")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # Lista llamadas encontradas
        self.__lista_llamadas = None

        # Gestor Asociado
        self.__gestor = None

        # Labels    
        self.__titulo_lbl = ctk.CTkLabel(master=self, text="Consultar Encuesta", font=(FUENTE, 23))
        self.__fecha_inicio_lbl = ctk.CTkLabel(master=self, text="Fecha Inicio", font=(FUENTE, 15))
        self.__fecha_fin_lbl = ctk.CTkLabel(master=self, text="Fecha Fin", font=(FUENTE, 15))
        self.__llamadas_encontradas_lbl = ctk.CTkLabel(master=self, text="Llamadas encontradas", font=(FUENTE, 15))
        
        # DateEntries
        self.__fecha_inicio_date_entry = tkc.DateEntry(master=self, selectmode="day")
        self.__fecha_fin_date_entry = tkc.DateEntry(master=self, selectmode="day")

        # Botones

        self.__comenzar_busqueda_btn = ctk.CTkButton(master=self, text="Buscar", font=(FUENTE, 23), command=self.evento_boton_buscar)
        self.__seleccionar_llamada_btn = ctk.CTkButton(master=self, text="Seleccionar", font=(FUENTE, 23), command=None)
        self.__cancelar_busqueda_btn = ctk.CTkButton(master=self, text="Cancelar", font=(FUENTE, 23), command=self.evento_boton_cancelar)

        # Combo Box
        self.__llamadas_encontradas_combo = ctk.CTkComboBox(master=self, values=[],
        height=35, width=400, hover=True)

        # Frame Datos Llamada
        # self.__lista_datos_llamada = FrameDatosLlamadaSeleccionada(master=self)

        # Top levels

        # Datos Llamada Seleccionada
        self.__datos_llamada_seleccionada_top_level = None
        # Cuando no se encuentras llamadas en el periodo
        self.__llamadas_no_encontradas_top_level = None
        # Cuando hay un error buscando los datos de la llamada seleccionada
        self.__datos_llamada_no_encontrados_top_level = None
        # Cuando se encuentra la llamada y se termina la consulta
        self.__fin_consulta_top_level = None
        # Cuando se genera el csv
        self.__csv_generado_top_level = None
        # Cuando se cancela la consulta
        self.__cancelacion_consulta_top_level = None
        

        # Si se aprieta la cruz
        self.protocol("WM_DELETE_WINDOW", lambda: exit())
    

    # Getter y Setter Gestor
    @property
    def gestor(self):
        return self.__gestor
    
    @gestor.setter
    def gestor(self, value):
        self.__gestor = value

    # lista llamadas encontradas
    @property
    def lista_llamadas(self):
        return self.__lista_llamadas
    
    @lista_llamadas.setter
    def lista_llamadas(self, value):
        self.__lista_llamadas = value



    # METODOS

    def mostrar_titulo(self):
        self.__titulo_lbl.grid(padx=15, pady=15 ,row=0, column=0, columnspan=4)

    def mostrar_input_fecha_inicio(self):
        self.__fecha_inicio_lbl.grid(padx=15, pady=15 ,row=1, column=0, columnspan=2)
        self.__fecha_inicio_date_entry.grid(padx=15, pady=15 ,row=2, column=0, columnspan=2)

    def mostrar_input_fecha_fin(self):
        self.__fecha_fin_lbl.grid(padx=15, pady=15 ,row=1, column=2, columnspan=2)
        self.__fecha_fin_date_entry.grid(padx=15, pady=15 ,row=2, column=2, columnspan=2)

    def mostrar_boton_buscar(self):
        self.__comenzar_busqueda_btn.grid(padx=15, pady=15 ,row=3, column=0, columnspan=4)

    def mostrar_lista_llamadas_encontradas(self):
        self.__llamadas_encontradas_lbl.grid(padx=15, pady=15, row=4, column=0, columnspan=4)
        self.__llamadas_encontradas_combo.grid(padx=15, pady=15, row=6, column=0, columnspan=4)
        self.__llamadas_encontradas_combo.set("No hay llamadas en periodo")
        self.__seleccionar_llamada_btn.grid(padx=15, pady=15, row=7, column=0, columnspan=4)

    def mostrar_boton_cancelacion(self):
        self.__cancelar_busqueda_btn.grid(padx=15, pady=15 ,row=8, column=0, columnspan=4)
    
    
    # Eventos de Boton
    
    def evento_boton_buscar(self):
        # Mensaje 4
        self.gestor.tomar_boton_buscar()
        # self.__gestor.tomar_periodo()
        # self.gestor.periodo_tomado()

    def evento_boton_seleccionar(self):
        self.gestor.tomar_boton_seleccionar()

    def evento_boton_cancelar(self):
        cancelacion_toplevel = MessageBoxTopLevel(self)
        cancelacion_toplevel.mostrar_mensaje("Cancelacion",
                                             "Se ha cancelado el caso de uso",
                                             "Cerrar")
        self.withdraw()



    # Metodos RCU

    # Mensaje 2
    def habilitar_ventana(self):
        self.mostrar_titulo()
        self.mostrar_input_fecha_inicio()
        self.mostrar_input_fecha_fin()
        self.mostrar_boton_buscar()
        self.mostrar_lista_llamadas_encontradas()
        self.mostrar_boton_cancelacion()
        self.mainloop()

    # Mensaje 4
    def solicitar_periodo(self):
        fecha_inicio = self.__fecha_inicio_date_entry.get()
        fecha_fin = self.__fecha_fin_date_entry.get()
        # Mensaje 7
        self.gestor.tomar_periodo(fecha_inicio, fecha_fin)
        # Mensaje previo al 8
        self.gestor.buscar_mostrar_llamadas()
    
    # Mensaje 12 y Mensaje 13
    def mostrar_llamadas_con_rta(self, lista_llamadas):
        # print("llamadas mostradas")
        print(lista_llamadas)
        self.lista_llamadas = lista_llamadas
        # Actualizar la combo box de la lista de las llamadas
        if lista_llamadas:
            # Activar el boton de seleccion
            self.__seleccionar_llamada_btn.configure(command=self.evento_boton_seleccionar)
            lista_a_mostrar = [from_call_dictionary_to_string(l) for l in lista_llamadas]
            self.__llamadas_encontradas_combo.configure(values=lista_a_mostrar)
            self.__llamadas_encontradas_combo.set(lista_a_mostrar[0])

    # Mensaje 13
    def solicitar_seleccion_llamada(self):
        llamada_seleccionada_string = self.__llamadas_encontradas_combo.get()
        # Mensaje 15
        self.gestor.tomar_seleccion_llamada(llamada_seleccionada_string)
        # Mensaje disparador del 16
        self.gestor.buscar_mostrar_datos_llamada()

    # Mensaje 34
    def mostrar_datos_llamada(self, datos_llamada):
        # Crear top level
        datos_llamada_toplevel = LlamadaSeleccionadaTopLevel(self)

        # Hacer bonitos los datos
        cliente = datos_llamada.get("cliente")
        estado_actual = datos_llamada.get("estado_actual")
        duracion = datos_llamada.get("duracion")
        preguntas = datos_llamada.get("datos_encuesta")
        encuesta = preguntas[0].get("encuesta")

        cliente = f"Nombre de cliente:    {cliente}"
        estado_actual_duracion = f"Estado actual: {estado_actual}\nDuracion: {duracion} minutos"
        encuesta = f"Encuesta: {encuesta}"
        preguntas = [ "Pregunta: " 
                     + str(l.get("pregunta")) 
                     + "\nRespuesta: "
                     + str(l.get("respuesta")) for l in preguntas]
        # print(preguntas)

        # Mostrar datos en top level
        datos_llamada_toplevel.mostrar_datos_llamada(cliente, estado_actual_duracion,
                                                     encuesta, preguntas)
        # Minimizar ventana actual (la del periodo)
        self.withdraw()
        



if __name__ == "__main__":
    pant = PantallaConsultarEncuesta()
    pant.habilitar_ventana()