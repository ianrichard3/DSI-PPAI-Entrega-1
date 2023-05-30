import customtkinter as ctk
import tkinter as tk


# importar message_box_TL

from message_box_top_level import MessageBoxTopLevel



class LlamadaSeleccionadaTopLevel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)

        self.geometry("900x700")
        self.resizable(False, False)
        self.title("Llamada Seleccionada")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Titulo
        self.__llamada_seleccionada_lbl = ctk.CTkLabel(master=self, text="Llamada Seleccionada")

        # Datos del Cliente
        self.__nombre_cliente_lbl = ctk.CTkLabel(master=self)

        # Datos de llamada (estado actual y duracion)
        self.__datos_llamada_lbl = ctk.CTkLabel(master=self)
        
        # Datos de la encuesta
        self.__datos_encuesta_lbl = ctk.CTkLabel(master=self)

        # Datos Preguntas
        self.__pregunta1_lbl = ctk.CTkLabel(master=self)
        self.__pregunta2_lbl = ctk.CTkLabel(master=self)
        self.__pregunta3_lbl = ctk.CTkLabel(master=self)

        # Botones
        self.__cerrar_btn = ctk.CTkButton(master=self, text="Cerrar", command=self.evento_boton_cerrar)
        self.__generar_csv_btn = ctk.CTkButton(master=self, text="Generar CSV", command=self.evento_boton_csv)

        # Top levels
        self.__toplevel_fin = None
        self.__toplevel_csv = None

        self.protocol("WM_DELETE_WINDOW", lambda: exit())

    # Metodos

    # Eventos de boton

    def evento_boton_cerrar(self):
        # Creacion del top level de finalizacion
        self.__toplevel_fin = MessageBoxTopLevel(self)
        self.__toplevel_fin.mostrar_mensaje("Consulta Finalizada", "Se ha finalizado la consulta de llamada", "Cerrar")
        self.withdraw()
        # Si se apreta el cerrar -> Se inutiliza el boton de generar csv
        # self.__generar_csv_btn.configure(command=None)

    def evento_boton_csv(self):
        self.__toplevel_csv = MessageBoxTopLevel(self)
        self.__toplevel_csv.mostrar_mensaje("Consulta Finalizada", "Se ha generado el CSV \n'exitosamente'", "Aceptar")
        self.withdraw()
        # Si se apreta el generar csv -> Se inutiliza el boton de cerrar
        # self.__cerrar_btn.configure(command=None)



    # Actualizacion de datos de la pantalla 
    def mostrar_datos_llamada(self, nombre_cliente, datos_llamada, datos_encuesta, preguntas):
        # Titulo
        self.__llamada_seleccionada_lbl.grid(padx=15, pady=15, row=0, column=0, columnspan=2)

        # cliente-llamada-encuesta
        self.__nombre_cliente_lbl.configure(text=nombre_cliente, font=("Helvetica", 15), wraplength=200)
        self.__datos_llamada_lbl.configure(text=datos_llamada, font=("Helvetica", 15), wraplength=200)
        self.__datos_encuesta_lbl.configure(text=datos_encuesta, font=("Helvetica", 15), wraplength=200)
        # grid
        self.__nombre_cliente_lbl.grid(padx=15, pady=15, row=1, column=0)
        self.__datos_llamada_lbl.grid(padx=15, pady=15, row=2, column=0)
        self.__datos_encuesta_lbl.grid(padx=15, pady=15, row=3, column=0)

        # Preguntas
        self.__pregunta1_lbl.configure(text=preguntas[0], font=("Helvetica", 15), wraplength=200)
        self.__pregunta2_lbl.configure(text=preguntas[1], font=("Helvetica", 15), wraplength=200)
        # grid
        self.__pregunta1_lbl.grid(padx=15, pady=15, row=4, column=0)
        self.__pregunta2_lbl.grid(padx=15, pady=15, row=5, column=0)

        if len(preguntas) > 2:
            self.__pregunta3_lbl.configure(text=preguntas[2], font=("Helvetica", 15), wraplength=200)
            # grid
            self.__pregunta3_lbl.grid(padx=15, pady=15, row=6, column=0)

        # Botones
        self.__cerrar_btn.grid(padx=15, pady=15, row=7, column=0)
        self.__generar_csv_btn.grid(padx=15, pady=15, row=7, column=1)








if __name__ == "__main__":

    # PRUEBA

    app = ctk.CTk()
    top_level = LlamadaSeleccionadaTopLevel(app)
    top_level.mostrar_datos_llamada("El flaquito", "Estado: Inciado   \nDuracion: 3.2 minutos", "Encuesta: Encuesta 1", ["Como estas? Bien", "Muy mal? Si"])




    app.mainloop()
