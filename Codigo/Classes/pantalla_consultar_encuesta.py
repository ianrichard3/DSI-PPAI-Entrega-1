class Pantalla_consultar_encuesta:
    def __init__(self, lbl_fecha_inicio, lbl_fecha_fin, txt_fecha_inicio, txt_fecha_fin, btn_opcion_csv, combo_llamadas, lbl):
        self.__lbl_fecha_inicio = lbl_fecha_inicio
        self.__lbl_fecha_fin = lbl_fecha_fin
        self.__txt_fecha_inicio = txt_fecha_inicio
        self.__txt_fecha_fin = txt_fecha_fin
        self.__btn_opcion_csv = btn_opcion_csv
        self.__combo_llamadas = combo_llamadas
        self.__lbl = lbl

    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter fecha_inicio_periodo
    @property
    def lbl_fecha_inicio(self):
        return self.__fecha_inicio_periodo
    

