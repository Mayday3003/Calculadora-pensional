class ErrorBaseSettlementIncomeNegative(Exception):
    def __init__(self):
        super().__init__("El valor de ingreso_base_de_liquidacion no puede ser cero ni negativo. Por favor, ingrese un valor válido.")

class ErrorBaseSettlementIncomeLetras(Exception):
    def __init__(self):
        super().__init__("El valor de ingreso_base_de_liquidacion debe ser numérico. Por favor, ingrese un número válido.")

class ErrorPensionPorcentageNegative(Exception):
    def __init__(self):
        super().__init__("El porcentaje ingresado de su pensión no puede ser cero o menor, ingrese un valor válido")

class ErrorPensionPorcentageLetras(Exception):
    def __init__(self):
        super().__init__("El valor del porcentaje de pension debe ser numérico. Por favor, ingrese un número válido.")

class ErrorHighPensionPorcentage(Exception):
    def __init__(self):
        super().__init__("El valor del porcentaje de pension debe ser menor que cien. Por favor, ingrese un número válido.")

class ErrorCurrentLegalMinimumWageLetras(Exception):
    def __init__(self):
        super().__init__("El valor del SMMLV que ingresó se debe ingresar de forma numerica, porfavor ingrese un valor válido")

class ErrorCurrentLegalMinimumWageNegative(Exception):
    def __init__(self):
        super().__init__("""El valor del SMMLV ingresado no pude ser cero ni valores negativos""")

