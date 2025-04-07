from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Importar lógica y errores personalizados
from model.Pension_Calculate_Logic import calculate_pension
from model.Error_Pension import (
    ErrorBaseSettlementIncomeNegative,
    ErrorBaseSettlementIncomeLetras,
    ErrorPensionPorcentageNegative,
    ErrorPensionPorcentageLetras,
    ErrorHighPensionPorcentage,
    ErrorCurrentLegalMinimumWageLetras,
    ErrorCurrentLegalMinimumWageNegative
)

# Cargar la interfaz .kv
Builder.load_file("src/view/gui/pension_gui.kv")


class PensionLayout(BoxLayout):
    def calcular_pension_gui(self):
        ibl = self.ids.base_settlement_income.text
        porcentaje = self.ids.pension_percentage.text
        smmlv = self.ids.current_legal_minimum_wage.text

        self.restaurar_colores()

        try:
            resultado = calculate_pension(float(ibl), float(porcentaje), float(smmlv))
            self.ids.result_label.color = (0, 1, 0, 1)
            self.ids.result_label.text = f"Resultado: ${resultado:,.2f}"
            self.mostrar_popup_info("Cálculo exitoso", "La pensión fue calculada correctamente.")
        except Exception as e:
            self.ids.result_label.color = (1, 0, 0, 1)
            self.ids.result_label.text = "Error: Revise los campos"
            self.colorear_campos_error(e)
            self.mostrar_popup_error("Error de entrada", str(e))

    def colorear_campos_error(self, error):
        if isinstance(error, (ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras)):
            self.ids.base_settlement_income.background_color = (1, 0.7, 0.7, 1)
        if isinstance(error, (ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras, ErrorHighPensionPorcentage)):
            self.ids.pension_percentage.background_color = (1, 0.7, 0.7, 1)
        if isinstance(error, (ErrorCurrentLegalMinimumWageNegative, ErrorCurrentLegalMinimumWageLetras)):
            self.ids.current_legal_minimum_wage.background_color = (1, 0.7, 0.7, 1)

    def restaurar_colores(self):
        self.ids.base_settlement_income.background_color = (1, 1, 1, 1)
        self.ids.pension_percentage.background_color = (1, 1, 1, 1)
        self.ids.current_legal_minimum_wage.background_color = (1, 1, 1, 1)

    def limpiar_campos(self):
        self.ids.base_settlement_income.text = ""
        self.ids.pension_percentage.text = ""
        self.ids.current_legal_minimum_wage.text = ""
        self.ids.result_label.text = "Resultado: "
        self.ids.result_label.color = (0.5, 0.5, 0.5, 1)
        self.restaurar_colores()

    def mostrar_popup_error(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def mostrar_popup_info(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def mostrar_ayuda(self):
        texto_ayuda = (
            "Calculadora pensional:\n\n"
            "- IBL: Ingreso Base de Liquidación, salario promedio sobre el cual se liquida la pensión.\n"
            "- Porcentaje: Porcentaje usado para calcular la pensión (ej. 75%).\n"
            "- SMMLV: Salario Mínimo Mensual Legal Vigente.\n\n"
            "La pensión no puede ser inferior al SMMLV.\n"
        )
        contenido = ScrollView(size_hint=(1, 1))
        label = Label(text=texto_ayuda,
                      font_size=18,
                      size_hint_y=None,
                      halign="left",
                      valign="top")
        label.bind(texture_size=label.setter("size"))
        label.text_size = (Window.width * 0.7, None)
        contenido.add_widget(label)
        popup = Popup(title="Ayuda",
                      content=contenido,
                      size_hint=(0.8, 0.6))
        popup.open()


class PensionApp(App):
    def build(self):
        return PensionLayout()


if __name__ == "__main__":
    PensionApp().run()
