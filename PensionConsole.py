from PensionCalculateLogic import *
from ErrorPension import *


try:
    ibl= input("Ingrese el ibl:")
    pension_porcentage = input("Ingrese el porcentaje de pensión:")
    smmlv = input("Ingrese su salario minimo legal vigente:")

    if ibl.isnumeric():
        ibl = float(ibl)

    if pension_porcentage[0].isnumeric():
        pension_porcentage = float(pension_porcentage)

    if smmlv.isnumeric():
        smmlv = float(smmlv)
    
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

except ErrorCurrentLegalMinimumWageLetras as err:
    print(f"Oh no!, ha sucesido un error: {err}")

except ErrorCurrentLegalMinimumWageNegative as err:
    print(f"Oh no!, ha sucesido un error: {err}")   