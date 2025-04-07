from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import sys
import os

# Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Importar la lógica de cálculo y las excepciones personalizadas
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

# Cargar la interfaz KV (asegúrate que la ruta sea correcta)
Builder.load_file("src/view/gui/pension_gui.kv")


class PensionLayout(BoxLayout):
    def calcular_pension_gui(self):
        # Obtener y limpiar los textos de los campos
        ibl = self.ids.base_settlement_income.text.strip()
        porcentaje = self.ids.pension_percentage.text.strip()
        smmlv = self.ids.current_legal_minimum_wage.text.strip()

        self.restaurar_colores()

        try:
            # Verificar que ningún campo esté vacío
            if not ibl or not porcentaje or not smmlv:
                raise ValueError("Todos los campos deben estar completos.")

            # Convertir a float y realizar el cálculo
            resultado = calculate_pension(float(ibl), float(porcentaje), float(smmlv))
            self.ids.result_label.color = (0, 1, 0, 1)  # Verde para éxito
            self.ids.result_label.text = f"Resultado: ${resultado:,.2f}"
            self.mostrar_popup_info("Cálculo exitoso", "La pensión fue calculada correctamente.")

        except (ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras,
                ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras,
                ErrorHighPensionPorcentage, ErrorCurrentLegalMinimumWageLetras,
                ErrorCurrentLegalMinimumWageNegative, ValueError) as e:
            self.ids.result_label.color = (1, 0, 0, 1)  # Rojo para error
            self.ids.result_label.text = "Error: Revise los campos"
            self.colorear_campos_error(e)
            self.mostrar_popup_error("Error de entrada", str(e))
        except Exception as e:
            # Manejo de cualquier otro error inesperado
            self.ids.result_label.color = (1, 0, 0, 1)
            self.ids.result_label.text = "Error: Revise los campos"
            self.mostrar_popup_error("Error inesperado", str(e))

    def colorear_campos_error(self, error):
        # Color rojo oscuro para mantener la estética del modo oscuro
        color_error = (0.4, 0.1, 0.1, 1)
        # Si se lanza un ValueError (por ejemplo, campo vacío), coloreamos los campos vacíos
        if isinstance(error, ValueError):
            if not self.ids.base_settlement_income.text.strip():
                self.ids.base_settlement_income.background_color = color_error
            if not self.ids.pension_percentage.text.strip():
                self.ids.pension_percentage.background_color = color_error
            if not self.ids.current_legal_minimum_wage.text.strip():
                self.ids.current_legal_minimum_wage.background_color = color_error
        else:
            if isinstance(error, (ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras)):
                self.ids.base_settlement_income.background_color = color_error
            if isinstance(error, (ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras, ErrorHighPensionPorcentage)):
                self.ids.pension_percentage.background_color = color_error
            if isinstance(error, (ErrorCurrentLegalMinimumWageNegative, ErrorCurrentLegalMinimumWageLetras)):
                self.ids.current_legal_minimum_wage.background_color = color_error

    def restaurar_colores(self):
        # Restaurar al color oscuro base (modo oscuro)
        color_base = (0.2, 0.2, 0.2, 1)
        self.ids.base_settlement_income.background_color = color_base
        self.ids.pension_percentage.background_color = color_base
        self.ids.current_legal_minimum_wage.background_color = color_base

    def limpiar_campos(self):
        self.ids.base_settlement_income.text = ""
        self.ids.pension_percentage.text = ""
        self.ids.current_legal_minimum_wage.text = ""
        self.ids.result_label.text = "Resultado: "
        self.ids.result_label.color = (0.5, 0.5, 0.5, 1)
        self.restaurar_colores()

    def mostrar_popup_error(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje, font_size="16sp"),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def mostrar_popup_info(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje, font_size="16sp"),
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
