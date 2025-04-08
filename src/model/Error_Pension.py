# -------------------- ERRORES: INGRESO BASE DE LIQUIDACIÓN (IBL) --------------------

class ErrorBaseSettlementIncomeNegative(Exception):
    """
    Se lanza cuando el ingreso base de liquidación es menor o igual a cero.
    """
    def __init__(self):
        super().__init__("El ingreso base de liquidación no puede ser negativo ni cero.")


class ErrorBaseSettlementIncomeLetras(Exception):
    """
    Se lanza cuando el ingreso base de liquidación contiene letras o caracteres no válidos.
    """
    def __init__(self):
        super().__init__("El ingreso base de liquidación no debe contener letras ni símbolos.")


# -------------------- ERRORES: PORCENTAJE DE PENSIÓN --------------------

class ErrorPensionPorcentageNegative(Exception):
    """
    Se lanza cuando el porcentaje de pensión es menor o igual a cero.
    """
    def __init__(self):
        super().__init__("El porcentaje de pensión no puede ser negativo ni cero.")


class ErrorPensionPorcentageLetras(Exception):
    """
    Se lanza cuando el porcentaje de pensión contiene letras o caracteres no válidos.
    """
    def __init__(self):
        super().__init__("El porcentaje de pensión no debe contener letras ni símbolos.")


class ErrorHighPensionPorcentage(Exception):
    """
    Se lanza cuando el porcentaje de pensión es igual o superior al 100%.
    """
    def __init__(self):
        super().__init__("El porcentaje de pensión no puede ser igual o mayor al 100%.")


# -------------------- ERRORES: SALARIO MÍNIMO LEGAL VIGENTE (SMMLV) --------------------

class ErrorCurrentLegalMinimumWageLetras(Exception):
    """
    Se lanza cuando el salario mínimo legal vigente contiene letras o caracteres no válidos.
    """
    def __init__(self):
        super().__init__("El salario mínimo legal vigente no debe contener letras ni símbolos.")


class ErrorCurrentLegalMinimumWageNegative(Exception):
    """
    Se lanza cuando el salario mínimo legal vigente es menor o igual a cero.
    """
    def __init__(self):
        super().__init__("El salario mínimo legal vigente no puede ser negativo ni cero.")
