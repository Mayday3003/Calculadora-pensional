## Nombres de los creadores del repositorio: 
- Kevin Mateo Gomez Diez
- Sara Rojas Martínez

## Nombres, segunda entrega:
- Heiver David Ruales Luna
- Mariana Lopera Correa

# Calculadora-pensional
En este repositorio se podrá encontrar toda la información acerca de la calculadora pensional, este proyecto tiene como objetivo proporcionar una herramienta intuitiva y eficiente para calcular la pensión y simulaciones personalizas para cada usuario. 

Entrevista sobre las pensiones: https://drive.google.com/file/d/1enmZgatAiFyT37SUNeuEhobB0pi-XEJx/view?usp=sharing

El cálculo de la pensión se basa en el Ingreso Base de Liquidación (IBL) y la tasa de reemplazo, que depende del número de semanas cotizadas y del IBL en relación con el Salario Mínimo Legal Vigente.


## Arquitectura:
El proyecto tiene una estructura donde todos los archivos estan separados por carpetas las cuales son: model, view\console y test. Además, hay un archivo .gitignore el cual a la hora de hacer los commits y los pushs va a ignorar las carpetas con nombre __pycache__.
También, se agregó un archivo de excel el cual tiene la información de los casos de prueba de la calculadora pensional. 


## Requisitos
- Python 3.9 o superior
- Kivy 2.3.1

### Instalar dependencias

```bash
pip install kivy==2.3.1
```

## Instrucciones para ejecutar las pruebas unitarias:
* Se ingresa a la carpeta test
* Luego, se ingresa al archivo Pension_Calculate_Test.py
* Y por último, se ejecuta el código

## Instrucciones para ejecutar la interfaz de Consola:
* Se ingresa a la carpeta view\console
* Se accede a la carpeta console
* Se ingresa al archivo Pension_Console.py
* Se ejecuta el código
* Se ingresa el valor del ibl
* Despues, se ingresa el valor del porcentaje de pensión
* Luego, se ingresa el valor del salario mínimo legal vigente
* Y por ultimo se muestra el valor total de la pensión


## Instrucciones para generar el ejecutable en Linux

### Requisitos adicionales

- PyInstaller

Instalación:

```bash
pip install pyinstaller
```

### Procedimiento

1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/Calculadora-pensional.git
cd Calculadora-pensional
```

2. Dar permisos de ejecución al script:

```bash
chmod +x install.sh
```

3. Ejecutar el script para construir el ejecutable e instalar el acceso directo:

```bash
./install.sh
```

El script realizará las siguientes acciones:

- Instalará las dependencias necesarias.
- Generará el ejecutable en `dist/CalculadoraPensional/CalculadoraPensional`.
- Creará un acceso directo en el sistema operativo Linux.
- Actualizará la base de datos de aplicaciones para que la aplicación pueda ser buscada en el menú del sistema.

### Ejecución de la aplicación instalada

Una vez completada la instalación:

- Buscar la aplicación "Calculadora Pensional" en el menú de aplicaciones del sistema operativo.
- O alternativamente, ejecutar el archivo directamente desde la terminal:

```bash
./dist/CalculadoraPensional/CalculadoraPensional
```

Asegúrate de tener permisos de ejecución sobre el archivo si es necesario.

---



### Ejecutar la GUI

```bash
python src/view/gui/Pension_Gui.py
```

La ventana se abrirá con una interfaz gráfica donde puedes ingresar los valores requeridos.

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
* Se muestra el total de la pensión mensual

## Como ejecutar desde consola/terminal:
e clona el proyecto luego ingresa a la carpeta raiz (calculadora-pensional), desde la terminal usando el comando "cd" y se pone la ruta en donde se guardo la carpeta raiz, la ruta se obtine copiando la direccion desde la carpeta raiz, y desde la teminal se ejecuta el siguiente comando:
```
py src\view\console\Pension_Console.py
```

## Como ejecutar las pruebas (test) desde la teminal:
Se clona el proyecto luego ingresa a la carpeta raiz (calculadora-pensional), desde la terminal usando el comando "cd" y se pone la ruta en donde se guardo la carpeta raiz, la ruta se obtine copiando la direccion desde la carpeta raiz, y desde la teminal se ejecuta el siguiente comando:
```
py test\Pension_Calculate_Test.py
```

## Instrucciones para ejecutar la interfaz gráfica (GUI):
Asegúrate de tener instalado el framework Kivy. Si no lo tienes, instálalo con el siguiente comando:
```
pip install kivy
```
Luego, sigue estos pasos:
1. Clona el repositorio y navega a la carpeta raíz del proyecto (calculadora-pensional) desde la terminal.
2. Desde la terminal, ejecuta el siguiente comando para abrir la interfaz gráfica:
```
py src/view/gui/pension_gui.py
```
Se abrirá una ventana en la que deberás ingresar:

- El Ingreso Base de Liquidación (IBL).

- El Porcentaje de pensión que aplicarás al IBL.

- El Salario Mínimo Mensual Legal Vigente (SMMLV) (este se autocompleta con el valor por defecto de $1,300,000, por lo que no es necesario modificarlo).

Haz clic en "Calcular" para obtener el valor estimado de la pensión mensual.


También puedes usar el botón "Limpiar" para reiniciar los campos o "Ayuda" para ver una explicación detallada del funcionamiento de la calculadora.
