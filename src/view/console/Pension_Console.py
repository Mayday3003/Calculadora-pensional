import sys
sys.path.append("src")

from model.Pension_Calculate_Logic import *
from model.Error_Pension import *

try:
    ibl= input("Ingrese la base de liquidacion:")
    pension_porcentage = input("Ingrese el porcentaje de pensión:")
    smmlv = input("Ingrese su salario minimo legal vigente:")
    
    mensual_pension = calculate_pension(ibl, pension_porcentage, smmlv)
    
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
