class ErrorIblNegative(Exception):
    """El valor de IBL no puede ser cero ni negativo. Por favor, ingrese un valor válido."""

class ErroIblLetras(Exception):
    """El valor de IBL debe ser numérico. Por favor, ingrese un número válido."""

class ErrorPensionPorcentageCero(Exception):
    """El porcentaje ingresado de su pensión no puede ser cero o menor, ingrese un valor válido"""

class ErrorSmmlvLetras(Exception):
    """El valor del SMMLV que ingresó se debe ingresar de forma numerica, porfavor ingrese un valor válido"""

class ErrorSmmlvMenor(Exception):
    """El valor del SMMLV ingresado no pude ser cero ni valores negativos"""