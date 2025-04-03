from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")
from model.Pension_Calculate_Logic import calculate_pension


class PensionApp(App):
    def build(self):

        contenedor = GridLayout(cols = 2)

        contenedor.add_widget(Label(text = 'Ingrese la base de liquidacion:'))
        self.liquidacion = TextInput()
        contenedor.add_widget(self.liquidacion)

        contenedor.add_widget(Label(text = 'Ingrese el porcentaje de pensión:'))
        self.pension_porcentage = TextInput()
        contenedor.add_widget(self.pension_porcentage)

        contenedor.add_widget(Label(text = 'Ingrese su salario minimo legal vigente:'))
        self.salario_minimo = TextInput()
        contenedor.add_widget(self.salario_minimo)

        self.resultado = Label()
        contenedor.add_widget(self.resultado)

        boton_calcular = Button(text = 'Calcular')
        contenedor.add_widget(boton_calcular)
        boton_calcular.bind(on_press = self.calcular)

        return contenedor
    
    def calcular(self, sender):
        ingreso_base_de_liquidacion = float(self.liquidacion.text)
        pension_porcentage = float(self.pension_porcentage.text)
        salario_minimo_legal_vigente = float(self.salario_minimo.text)
        result = calculate_pension(ingreso_base_de_liquidacion, pension_porcentage, salario_minimo_legal_vigente)
        self.resultado.text = str(round(result, 2))
    
    
    
if __name__ == "__main__":
    PensionApp().run()