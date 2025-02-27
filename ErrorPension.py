class ErrorIblNegative(Exception):
    def __init__(self):
        super().__init__("El valor de IBL no puede ser cero ni negativo. Por favor, ingrese un valor válido.")
    

class ErroIblLetras(Exception):
    def __init__(self):
        super().__init__("""El valor de IBL debe ser numérico. Por favor, ingrese un número válido.""")

class ErrorPensionPorcentageCero(Exception):
    def __init__(self):
        super().__init__("""El porcentaje ingresado de su pensión no puede ser cero o menor, ingrese un valor válido""")
    

class ErrorSmmlvLetras(Exception):
    def __init__(self):
        super().__init__("""El valor del SMMLV que ingresó se debe ingresar de forma numerica, porfavor ingrese un valor válido""")
    

class ErrorSmmlvMenor(Exception):
    def __init__(self):
        super().__init__("""El valor del SMMLV ingresado no pude ser cero ni valores negativos""")

class ErrorPensionPorcentageLetras(Exception):
    def __init__(self):
        super().__init__("""El valor del porcentaje de pension debe ser numérico. Por favor, ingrese un número válido.""")