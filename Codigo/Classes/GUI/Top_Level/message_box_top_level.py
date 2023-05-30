import customtkinter as ctk
import tkinter as tk



class MessageBoxTopLevel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)

        self.geometry("250x200")
        self.resizable(False, False)


        self.__mensaje_lbl = ctk.CTkLabel(master=self)

        self.__boton = ctk.CTkButton(master=self)

        # Si se aprieta la x
        self.protocol("WM_DELETE_WINDOW", lambda: exit())

    def evento_boton(self):
        exit()

    def mostrar_mensaje(self, titulo_mensaje, mensaje, texto_boton):
        self.title(titulo_mensaje)
        self.__mensaje_lbl.configure(text=mensaje, font=("Helvetica", 15), wraplength=200)
        self.__boton.configure(text=texto_boton, font=("Helvetica", 15), command=self.evento_boton)
        self.__mensaje_lbl.pack(padx=20, pady=20, anchor="n")
        self.__boton.pack(padx=20, pady=10, anchor="s")
        # self.__mensaje_lbl.configure(text=mensaje, font=("Helvetica", 15), wraplength=200)



if __name__ == "__main__":

    #Mensaje para el momento en el que busquemos llamadas y no se encuentren...
    pant = ctk.CTk()
    mbtp = MessageBoxTopLevel(pant)
    mbtp.mostrar_mensaje("Llamadas en periodo", "No se han encontrado llamadas con encuestas respondidas en el periodo seleccionado", "Aceptar")
    # pant.mainloop()

    # pant = ctk.CTk()
    mbtp1 = MessageBoxTopLevel(pant)
    mbtp1.mostrar_mensaje("Error", "No se encontraron datos de la llamada", "Cerrar")
    # pant.mainloop()

    #Mensaje de cancelacion para el momento en el que se cancele la busqueda de una llamada o momento previo a crear un CSV
    # pant = ctk.CTk()
    mbtp_cancelar_llamada = MessageBoxTopLevel(pant)
    mbtp_cancelar_llamada.mostrar_mensaje("Cancelacion", "Se ha finalizado la busqueda de una llamada", "Aceptar")
    # pant.mainloop()

    # pant = ctk.CTk()
    mbtp_aceptacion = MessageBoxTopLevel(pant)
    mbtp_aceptacion.mostrar_mensaje("Aceptacion", "Se ha generado el CSV \n'exitosamente' ", "Ok")
    pant.mainloop()