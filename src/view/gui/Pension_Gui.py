from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from model.Pension_Calculate_Logic import calculate_pension
from model.Error_Pension import (
    ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras,
    ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras,
    ErrorHighPensionPorcentage, ErrorCurrentLegalMinimumWageLetras,
    ErrorCurrentLegalMinimumWageNegative
)

Builder.load_file("src/view/gui/pension_gui.kv")

class PensionLayout(BoxLayout):
    DEFAULT_SMMLV = 1_300_000

    def calcular_pension_gui(self):
        ibl_str = self.ids.base_settlement_income.text.strip()
        porcentaje_str = self.ids.pension_percentage.text.strip()
        smmlv_str = self.ids.current_legal_minimum_wage.text.strip()

        self.restaurar_colores()
        try:
            if not ibl_str or not porcentaje_str or not smmlv_str:
                raise ValueError("Todos los campos deben estar completos.")

            ibl = self._to_float(ibl_str, ErrorBaseSettlementIncomeLetras)
            porcentaje = self._to_float(porcentaje_str, ErrorPensionPorcentageLetras)
            smmlv = self._to_float(smmlv_str, ErrorCurrentLegalMinimumWageLetras)

            if smmlv != self.DEFAULT_SMMLV:
                self.ids.current_legal_minimum_wage.background_color = (0.5, 0.1, 0.1, 1)
                self.mostrar_popup("Error SMMLV",
                    f"El SMMLV debe ser {self.DEFAULT_SMMLV:,}. Se restablecerá al valor por defecto.")
                smmlv = self.DEFAULT_SMMLV
                self.ids.current_legal_minimum_wage.text = str(self.DEFAULT_SMMLV)

            if ibl <= 0:
                raise ErrorBaseSettlementIncomeNegative()
            if porcentaje <= 0:
                raise ErrorPensionPorcentageNegative()
            if porcentaje >= 100:
                raise ErrorHighPensionPorcentage()

            resultado = calculate_pension(ibl, porcentaje, smmlv)
            self.ids.result_label.color = (0.2, 0.8, 0.2, 1)  # Verde claro
            self.ids.result_label.text = f"Resultado: ${resultado:,.2f}"
            self.mostrar_popup("Cálculo exitoso", "La pensión fue calculada correctamente.")

        except Exception as e:
            self.colorear_campos_error(e)
            title = "Error de entrada" if isinstance(e, (
                ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras,
                ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras,
                ErrorHighPensionPorcentage, ErrorCurrentLegalMinimumWageLetras,
                ValueError)) else "Error inesperado"
            self.ids.result_label.color = (1, 0, 0, 1)
            self.ids.result_label.text = "Error: Revise los campos"
            self.mostrar_popup(title, str(e))

    def _to_float(self, text, exc):
        try:
            return float(text)
        except:
            raise exc()

    def colorear_campos_error(self, e):
        error_color = (0.5, 0.1, 0.1, 1)  # Rojo oscuro estilizado
        if isinstance(e, (ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras, ValueError)):
            self.ids.base_settlement_income.background_color = error_color
        if isinstance(e, (ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras, ErrorHighPensionPorcentage, ValueError)):
            self.ids.pension_percentage.background_color = error_color
        if isinstance(e, (ErrorCurrentLegalMinimumWageNegative, ErrorCurrentLegalMinimumWageLetras, ValueError)):
            self.ids.current_legal_minimum_wage.background_color = error_color

    def restaurar_colores(self):
        normal_color = (0.3, 0.3, 0.3, 1)  # Gris más claro y accesible
        self.ids.base_settlement_income.background_color = normal_color
        self.ids.pension_percentage.background_color = normal_color
        self.ids.current_legal_minimum_wage.background_color = normal_color

    def limpiar_campos(self):
        self.ids.base_settlement_income.text = ""
        self.ids.pension_percentage.text = ""
        self.ids.current_legal_minimum_wage.text = str(self.DEFAULT_SMMLV)
        self.ids.result_label.text = "Resultado: "
        self.ids.result_label.color = (0.6, 0.6, 0.6, 1)  # Gris neutral
        self.restaurar_colores()

    def mostrar_popup(self, title, msg):
        scroll = ScrollView(size_hint=(1, None), size=(400, 200))
        lbl = Label(text=msg, markup=True, font_size="16sp",
                    size_hint_y=None, text_size=(380, None))
        lbl.bind(texture_size=lambda inst, ts: setattr(lbl, 'height', ts[1]))
        scroll.add_widget(lbl)
        popup = Popup(title=title, content=scroll,
                      size_hint=(None, None), size=(420, 260))
        popup.open()

    def mostrar_ayuda(self):
        texto = (
            "Bienvenido a la Calculadora Pensional\n\n"
            "Esta herramienta te ayuda a estimar el valor aproximado de tu pensión mensual.\n\n"
            "¿Qué debes ingresar?\n"
            "1. IBL (Ingreso Base de Liquidación):\n"
            "   Es el promedio de tus salarios durante los últimos años antes de jubilarte. "
            "Por ejemplo, si ganabas $2.500.000 en promedio, escríbelo allí.\n\n"
            "2. Porcentaje de pensión (%):\n"
            "   Es el porcentaje del IBL que recibirás como pensión. Esto depende de tus años cotizados. "
            "Por ejemplo, podrías recibir el 65% de tu IBL. Si no sabes tu porcentaje exacto, puedes estimarlo.\n\n"
            "3. SMMLV (Salario Mínimo Mensual Legal Vigente):\n"
            "   Es un valor fijo de referencia establecido por el gobierno. "
            "Esta calculadora ya lo incluye automáticamente, por lo que no necesitas modificarlo.\n\n"
            "Una vez ingreses los valores, presiona 'Calcular' para ver el resultado.\n"
            "Si deseas borrar todo y empezar de nuevo, haz clic en 'Limpiar'."
        )
        self.mostrar_popup("Ayuda", texto)


class PensionApp(App):
    def build(self):
        return PensionLayout()

if __name__ == '__main__':
    PensionApp().run()
