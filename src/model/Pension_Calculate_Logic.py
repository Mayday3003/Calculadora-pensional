import sys
sys.path.append("src")  # Asegura que el módulo pueda importar desde el directorio 'src'

# Importa las excepciones personalizadas relacionadas al cálculo de pensión
from model.Error_Pension import (
    ErrorBaseSettlementIncomeNegative,
    ErrorBaseSettlementIncomeLetras,
    ErrorPensionPorcentageNegative,
    ErrorPensionPorcentageLetras,
    ErrorHighPensionPorcentage,
    ErrorCurrentLegalMinimumWageLetras,
    ErrorCurrentLegalMinimumWageNegative
)


def calculate_pension(ingreso_base_de_liquidacion: float, pension_porcentage: float, salario_minimo_legal_vigente: float) -> float:
    """
    Calcula la pensión mensual con base en el ingreso base de liquidación (IBL),
    el porcentaje de pensión y el salario mínimo mensual legal vigente (SMMLV).

    Parámetros:
        ingreso_base_de_liquidacion (float): Salario promedio sobre el cual se liquida la pensión (IBL).
        pension_porcentage (float): Porcentaje de liquidación de pensión (ej: 75%).
        salario_minimo_legal_vigente (float): Monto del SMMLV actual.

    Retorna:
        float: El valor final de la pensión mensual (mínimo el SMMLV).

    Excepciones:
        Lanza excepciones personalizadas si los valores son inválidos (negativos, no numéricos, etc.).
    """

    # ---------------- VALIDACIONES DEL INGRESO BASE DE LIQUIDACIÓN (IBL) ----------------

    # Verifica si el ingreso base de liquidación no es un número (por ejemplo, letras)
    if isinstance(ingreso_base_de_liquidacion, str):
        raise ErrorBaseSettlementIncomeLetras()
    
    # Verifica si el ingreso base de liquidación es menor o igual a cero
    if ingreso_base_de_liquidacion <= 0:
        raise ErrorBaseSettlementIncomeNegative()
    

    # ---------------- VALIDACIONES DEL PORCENTAJE DE PENSIÓN ----------------

    # Verifica si el porcentaje es un texto no convertible a número
    if isinstance(pension_porcentage, str):
        raise ErrorPensionPorcentageLetras()
    
    # Verifica si el porcentaje es menor o igual a cero
    if pension_porcentage <= 0:
        raise ErrorPensionPorcentageNegative()
    
    # Verifica si el porcentaje es 100 o más (no tendría sentido una pensión del 100%)
    if pension_porcentage >= 100:
        raise ErrorHighPensionPorcentage()


    # ---------------- VALIDACIONES DEL SALARIO MÍNIMO LEGAL VIGENTE (SMMLV) ----------------

    # Verifica si el salario mínimo es texto
    if isinstance(salario_minimo_legal_vigente, str):
        raise ErrorCurrentLegalMinimumWageLetras()
    
    # Verifica si el salario mínimo es cero o negativo
    if salario_minimo_legal_vigente <= 0:
        raise ErrorCurrentLegalMinimumWageNegative()


    # ---------------- CÁLCULO FINAL ----------------

    # Se realiza el cálculo de la pensión aplicando el porcentaje sobre el ingreso base
    resultado = ingreso_base_de_liquidacion * (pension_porcentage / 100)

    # Si el resultado es menor que el salario mínimo, se ajusta al mínimo legal
    if resultado < salario_minimo_legal_vigente:
        resultado = salario_minimo_legal_vigente

    return resultado
