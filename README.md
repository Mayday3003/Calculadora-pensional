# Calculadora-pensional
En este repositorio se podrá encontrar toda la información acerca de la calculadora pensional, este proyecto tiene como objetivo proporcionar una herramienta intuitiva y eficiente para calcular la pensión y simulaciones personalizas para cada usuario. 

Entrevista sobre las pensiones: https://drive.google.com/file/d/1enmZgatAiFyT37SUNeuEhobB0pi-XEJx/view?usp=sharing

** El cálculo de la pensión se basa en el Ingreso Base de Liquidación (IBL) y la tasa de reemplazo, que depende del número de semanas cotizadas y del IBL en relación con el Salario Mínimo Legal Vigente.

## Arquitectura:
El proyecto tiene una estructura donde todos los archivos estan separados por carpetas las cuales son: model, view\console y test. Además, hay un archivo .gitignore el cual a la hora de hacer los commits y los pushs va a ignorar las carpetas con nombre __pycache__.
También, se agregó un archivo de excel el cual tiene la información de los casos de prueba de la calculadora pensional. 

## Intrucciones para ejercutar las pruebas unitarias:
* Se ingresa a la carpeta test
* Luego, se ingresa al archivo Pension_Calculate_Test.py
* Y por último, se ejecuta el código

## Intrucciones para ejercutar la interfaz de Consola:
* Se ingresa a la carpeta view\console
* Se accede a la carpeta console
* Se ingresa al archivo Pension_Console.py
* Se ejecuta el código
* Se ingresa el valor del ibl
* Despues, se ingresa el valor del porcentaje de pensión
* Luego, se ingresa el valor del salario mínimo legal vigente
* Y por ultimo se muestra el valor total de la pensión

## Entradas:
* Base de liquidación
* Porcentaje de pensión
* Salario minimo legal vigente

## Proceso:
* Se ejecuta el archivo Pension_Console.py para iniciar la ejecución
* Se ingresan los valores pedidos
* El programa convierte los valores a floats
* Se calcula la tasa de remplazo
* Se multiplica el ingreso de base de liquidación por la tasa de remplazo

## Salidas:
* Se muestra el total de la pensión mesual

## Como ejecutar desde consola/terminal
Se ingresa a la carpeta raiz (calculadora-pensional) y desde la teminal se ejecuta el siguiente comando:
"""py src\view\console\Pension_Console.py"""

##Nombres de los creadores del repositorio: 

- Kevin Mateo Gomez Diez
- Sara Rojas Martínez
