from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")


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
        #calcular.bind(on_press = self.)

        return contenedor
    
    # def calcular(self, value):
    #     try:
    #         self.
    
    
    
if __name__ == "__main__":
    PensionApp().run()