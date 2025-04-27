# Importaciones necesarias de Kivy y otras librerías estándar
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import sys, os

# Agrega el directorio raíz del proyecto al path para poder importar módulos del modelo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Importa la lógica de cálculo de pensión y las clases de errores personalizados
from model.Pension_Calculate_Logic import calculate_pension
from model.Error_Pension import (
    ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras,
    ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras,
    ErrorHighPensionPorcentage, ErrorCurrentLegalMinimumWageLetras,
    ErrorCurrentLegalMinimumWageNegative
)

# Carga la interfaz desde el archivo .kv
kv_path = os.path.join(os.path.dirname(__file__), "pension_gui.kv")
Builder.load_file(kv_path)

# Clase que define el layout principal de la GUI
class PensionLayout(BoxLayout):
    # Valor por defecto del SMMLV (Salario Mínimo Mensual Legal Vigente)
    DEFAULT_SMMLV = 1_300_000

    # Función que se ejecuta al presionar el botón "Calcular"
    def calcular_pension_gui(self):
        # Obtiene los textos de los campos del formulario
        ibl_str = self.ids.base_settlement_income.text.strip()
        porcentaje_str = self.ids.pension_percentage.text.strip()
        smmlv_str = self.ids.current_legal_minimum_wage.text.strip()

        # Restaura los colores de los campos a su estado normal
        self.restaurar_colores()
        try:
            # Verifica que todos los campos estén llenos
            if not ibl_str or not porcentaje_str or not smmlv_str:
                raise ValueError("Todos los campos deben estar completos.")

            # Convierte los textos a float validando tipos
            ibl = self._to_float(ibl_str, ErrorBaseSettlementIncomeLetras)
            porcentaje = self._to_float(porcentaje_str, ErrorPensionPorcentageLetras)
            smmlv = self._to_float(smmlv_str, ErrorCurrentLegalMinimumWageLetras)

            # Si el valor ingresado para SMMLV es diferente al esperado, lo corrige
            if smmlv != self.DEFAULT_SMMLV:
                self.ids.current_legal_minimum_wage.background_color = (0.5, 0.1, 0.1, 1)
                self.mostrar_popup("Error SMMLV",
                    f"El SMMLV debe ser {self.DEFAULT_SMMLV:,}. Se restablecerá al valor por defecto.")
                smmlv = self.DEFAULT_SMMLV
                self.ids.current_legal_minimum_wage.text = str(self.DEFAULT_SMMLV)

            # Validaciones de negocio
            if ibl <= 0:
                raise ErrorBaseSettlementIncomeNegative()
            if porcentaje <= 0:
                raise ErrorPensionPorcentageNegative()
            if porcentaje >= 100:
                raise ErrorHighPensionPorcentage()

            # Cálculo de la pensión
            resultado = calculate_pension(ibl, porcentaje, smmlv)

            # Muestra el resultado en la interfaz
            self.ids.result_label.color = (0.2, 0.8, 0.2, 1)  # Verde claro
            self.ids.result_label.text = f"Resultado: ${resultado:,.2f}"
            self.mostrar_popup("Cálculo exitoso", "La pensión fue calculada correctamente.")

        except Exception as e:
            # Manejo de errores y visualización en la GUI
            self.colorear_campos_error(e)
            title = "Error de entrada" if isinstance(e, (
                ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras,
                ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras,
                ErrorHighPensionPorcentage, ErrorCurrentLegalMinimumWageLetras,
                ValueError)) else "Error inesperado"
            self.ids.result_label.color = (1, 0, 0, 1)
            self.ids.result_label.text = "Error: Revise los campos"
            self.mostrar_popup(title, str(e))

    # Intenta convertir un texto a float, lanza excepción personalizada si falla
    def _to_float(self, text, exc):
        try:
            return float(text)
        except:
            raise exc()

    # Cambia el color de fondo de los campos que tengan errores específicos
    def colorear_campos_error(self, e):
        error_color = (0.5, 0.1, 0.1, 1)  # Rojo oscuro estilizado
        if isinstance(e, (ErrorBaseSettlementIncomeNegative, ErrorBaseSettlementIncomeLetras, ValueError)):
            self.ids.base_settlement_income.background_color = error_color
        if isinstance(e, (ErrorPensionPorcentageNegative, ErrorPensionPorcentageLetras, ErrorHighPensionPorcentage, ValueError)):
            self.ids.pension_percentage.background_color = error_color
        if isinstance(e, (ErrorCurrentLegalMinimumWageNegative, ErrorCurrentLegalMinimumWageLetras, ValueError)):
            self.ids.current_legal_minimum_wage.background_color = error_color

    # Restaura los colores de todos los campos a un gris neutro
    def restaurar_colores(self):
        normal_color = (0.3, 0.3, 0.3, 1)  # Gris accesible
        self.ids.base_settlement_income.background_color = normal_color
        self.ids.pension_percentage.background_color = normal_color
        self.ids.current_legal_minimum_wage.background_color = normal_color

    # Limpia todos los campos del formulario y restaura valores por defecto
    def limpiar_campos(self):
        self.ids.base_settlement_income.text = ""
        self.ids.pension_percentage.text = ""
        self.ids.current_legal_minimum_wage.text = str(self.DEFAULT_SMMLV)
        self.ids.result_label.text = "Resultado: "
        self.ids.result_label.color = (0.6, 0.6, 0.6, 1)  # Gris neutral
        self.restaurar_colores()

    # Muestra un mensaje emergente tipo popup con un título y mensaje
    def mostrar_popup(self, title, msg):
        scroll = ScrollView(size_hint=(1, None), size=(400, 200))
        lbl = Label(text=msg, markup=True, font_size="16sp",
                    size_hint_y=None, text_size=(380, None))
        lbl.bind(texture_size=lambda inst, ts: setattr(lbl, 'height', ts[1]))
        scroll.add_widget(lbl)
        popup = Popup(title=title, content=scroll,
                      size_hint=(None, None), size=(420, 260))
        popup.open()

    # Muestra la sección de ayuda con instrucciones para el usuario
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

# Clase principal de la aplicación, lanza la GUI
class PensionApp(App):
    def build(self):
        return PensionLayout()

# Punto de entrada de la aplicación
if __name__ == '__main__':
    PensionApp().run()
