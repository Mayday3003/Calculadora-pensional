import sys
sys.path.append("src")

from model.Error_Pension import *

def calculate_pension(ingreso_base_de_liquidacion: float, pension_porcentage: float, salario_minimo_legal_vigente: float):
    
    # Se evalua si el ingreso base de liquidacion es un str y si es asi se muestra un error
    if type(ingreso_base_de_liquidacion) == str:
        raise ErrorBaseSettlementIncomeLetras()
    
    # Se evalua si el ingreso base de liquidacion es igual o menor a cero y si es asi se muestra un error
    if ingreso_base_de_liquidacion <= 0:
        raise ErrorBaseSettlementIncomeNegative()

    # Se evalua si el porcentaje de pension es un str y si es asi se muestra un error
    if type(pension_porcentage) == str:
        raise ErrorPensionPorcentageLetras()

    # Se evalua si el porcentaje de pension es igual o menor a cero y si es asi se muestra un error
    if pension_porcentage <= 0:
        raise ErrorPensionPorcentageNegative()

    # Se evalua si el porcentaje de pension es mayor a cien y si es asi se muestra un error
    if pension_porcentage > 100:
        raise ErrorHighPensionPorcentage()

    # Se evalua si el salario minimo legal vigente es un str y si es asi se muestra un error
    if type(salario_minimo_legal_vigente) == str:
        raise ErrorCurrentLegalMinimumWageLetras()
    
    # Se evalua si el salario minimo legal vigente es igual o menor a cero y si es asi se muestra un error
    if salario_minimo_legal_vigente <= 0:
        raise ErrorCurrentLegalMinimumWageNegative()
    
    # Se calcula el porcentaje de la pension
    pension_porcentage = pension_porcentage/100

    # Se realiza un calculo sobre la tasa de remplazo para calcular la pension
    tasa_remplazo = pension_porcentage-((0.5/100)*(ingreso_base_de_liquidacion/salario_minimo_legal_vigente))

    # Se multiplica el ingreso base de liquidacion por la tasa de remplazo y luego se retorna
    return ingreso_base_de_liquidacion*tasa_remplazo
