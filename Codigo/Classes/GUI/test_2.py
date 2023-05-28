import customtkinter as ctk
import tkinter as tk
import tkcalendar as tkc

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

class FrameDatosLlamadaSeleccionada(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Aca van los widgets del frame de los datos
        # De la llamada Seleccionada



class Pantalla(ctk.CTk):
    def __init__(self):
        super.__init__()
        self.geometry("800x600")
        self.title("TESTEANDO")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)


        # Labels    
        self.__titulo_lbl = ctk.CTkLabel(master=self)
        self.__fecha_hora_inicio_lbl = ctk.CTkLabel(master=self)
        self.__fecha_hora_fin_lbl = ctk.CTkLabel(master=self)
        
        # Text Boxes
        self.__fecha_hora_inicio_txt = ctk.CTkTextbox(master=self)
        self.__fecha_hora_fin_txt = ctk.CTkTextbox(master=self)


        # Combo Box
        self.__llamadas_encontradas_combo = ctk.CTkComboBox(master=self)


        # Frame Datos Llamada
        self.__lista_datos_llamada = FrameDatosLlamadaSeleccionada(master=self)



