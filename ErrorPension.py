class ErrorIblNegative(Exception):
    """El IBL no puede ser cero o menor"""

class ErroIblLetras(Exception):
    """El IBL se debe ingresar de forma numerica"""

class ErrorPensionPorcentageCero(Exception):
    """El porsentaje de su pension no puede cero o menor"""

class ErrorSmmlvLetras(Exception):
    """El SMMLV se debe ingresar de forma numerica"""

class ErrorSmmlvMenor(Exception):
    """El SMMLV no pude ser cero o menor"""