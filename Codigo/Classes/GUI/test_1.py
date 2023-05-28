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

# Main app setup

application = ctk.CTk()
application.geometry("750x600")
application.resizable(False, False)
application.title("Consultar Encuesta")
application.grid_columnconfigure(0, weight=1)
application.grid_columnconfigure(1, weight=1)
application.grid_columnconfigure(2, weight=1)
application.grid_columnconfigure(3, weight=1)

def title():
    title_consultar_encuesta = ctk.CTkLabel(
        master=application, text="Consultar Encuesta", font=("Helvetica", 24),
        justify="center"
    )
    title_consultar_encuesta.grid(row=0, column=0, pady=15, padx=5, columnspan=4)

title()

# Date

def start_date_input():
    label_date = ctk.CTkLabel(
        master=application, text="Fecha Inicio", font=("Helvetica", 15),
    )
    label_date.grid(row=1, column=0, pady=15, padx=5,)
    cal = tkc.DateEntry(application, selectmode='day')
    print(cal.get())
    cal.grid(row=1, column=1, padx=15)


start_date_input()

def end_date_input():
    label_date = ctk.CTkLabel(
        master=application, text="Fecha Fin", font=("Helvetica", 15),
    )
    label_date.grid(row=2, column=0, pady=15, padx=5,)
    cal = tkc.DateEntry(application, selectmode='day')
    cal.grid(row=2, column=1, padx=15)


end_date_input()


button_command = False

def search_function():
    print("searching")
    option_menu.configure(values=llamadas_array)  # 30 lines ahead
    option_menu.set("Llamadas Encontradas!")


def llamada_selected():
    print("Llamada selected:")
    print(option_menu.get())


def search_button():
    but = ctk.CTkButton(
        application, fg_color="#6DAFD5", bg_color="#6DAFD5", text="Search",
        font=("Helvetica", 15), corner_radius=8, border_width=0, command=search_function
    )
    but.grid(row=2, column=2, padx=10)


search_button()


option_menu = ctk.CTkOptionMenu(application)

def llamadas_found():

    label_llamadas = ctk.CTkLabel(
        master=application, text="Seleccione una llamada: ", font=("Helvetica", 15),
    )
    label_llamadas.grid(row=3, column=0, pady=15, padx=5)
    llamadas_frame = ctk.CTkFrame(
        master=application, fg_color=("#6DAFD5", "#5887A3"), height=200, width=500,
        corner_radius=10
    )
    llamadas_frame.grid(row=3, column=1, pady=15, padx=5, columnspan=3)
    # llamadas_frame.grid_columnconfigure(0, weight=1)
    # llamadas_frame.grid_columnconfigure(1, weight=1)
    # llamadas_frame.grid_columnconfigure(2, weight=1)
    # llamadas_frame.grid_columnconfigure(3, weight=1)

    # Options
    # RE MAL ESTO
    global option_menu
    option_menu = ctk.CTkOptionMenu(
        master=llamadas_frame, values=[], dynamic_resizing=False,
        height=35, width=400, hover=True
    )
    option_menu.set("Presiona Buscar")
    option_menu.pack(padx=10, pady=10)

    but_select = ctk.CTkButton(
        application, fg_color="#6DAFD5", bg_color="#6DAFD5", text="Select",
        font=("Helvetica", 15), corner_radius=8, border_width=0, command=llamada_selected
    )
    but_select.grid(row=4, column=2, padx=10)

# REQUIERE RE IMPLEMENTAR ESTO, ESTA HORRIBLE IMPLEMENTADO, PERO BUENO
# HAY QUE HACER TODO UNA CLASE GRANDE Y AHI SI SE PODRIA VER


llamadas_found()


# Run mainloop
application.mainloop()
