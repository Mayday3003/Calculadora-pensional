import sys
sys.path.append("src")

from model.Pension_Calculate_Logic import *
from model.Error_Pension import *

try:
    ingreso_base_de_liquidacion= input("Ingrese la base de liquidacion:")
    pension_porcentage = input("Ingrese el porcentaje de pensión:")
    salario_minimo_legal_vigente = input("Ingrese su salario minimo legal vigente:")
    
    if ingreso_base_de_liquidacion.isnumeric():
        ingreso_base_de_liquidacion = float(ingreso_base_de_liquidacion)

    if salario_minimo_legal_vigente.isnumeric():
        salario_minimo_legal_vigente = float(salario_minimo_legal_vigente)

    # Evalua si un el primer digito es un numero y convertira a pension porcentage en un float
    if pension_porcentage[0].isnumeric():
        pension_porcentage = float(pension_porcentage)
    
    # Evalua si un el segundo digito es un numero y convertira a pension porcentage en un float(caso para numeros negativos)
    elif pension_porcentage[1].isnumeric():
        pension_porcentage = float(pension_porcentage)

    mensual_pension = calculate_pension(ingreso_base_de_liquidacion, pension_porcentage, salario_minimo_legal_vigente)
    
    print(f"EL valor de tu pensión mensual es: {round(mensual_pension)}" )

except ErrorBaseSettlementIncomeNegative as err:
    print(f"Oh no!, ha sucesido un error: {err}")

except ErrorBaseSettlementIncomeLetras as err:
    print(f"Oh no!, ha sucesido un error: {err}")

except ErrorPensionPorcentageNegative as err:
    print(f"Oh no!, ha sucesido un error: {err}")

except ErrorPensionPorcentageLetras as err:
    print(f"Oh no!, ha sucesido un error: {err}")

except ErrorHighPensionPorcentage as err:
    print(f"Oh no!, ha sucesido un error: {err}")

except ErrorCurrentLegalMinimumWageLetras as err:
    print(f"Oh no!, ha sucesido un error: {err}")

except ErrorCurrentLegalMinimumWageNegative as err:
    print(f"Oh no!, ha sucesido un error: {err}")   
