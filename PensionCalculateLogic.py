from ErrorPension import *

def calculate_pension(ibl: float, pension_porcentage: float, smmlv: float):

    
    if type(ibl) == str:
        raise ErroIblLetras()

    if ibl <= 0:
        raise ErrorIblNegative()

    if pension_porcentage <= 0:
        raise ErrorPensionPorcentageCero

    if type(smmlv) == str:
        raise ErrorSmmlvLetras
    
    if smmlv <= 0:
        raise ErrorSmmlvMenor
    

    pension_porcentage = pension_porcentage/100
    tasa_remplazo = pension_porcentage-((0.5/100)*(ibl/smmlv))
    return ibl*tasa_remplazo
