def calculate_pension(ibl: float, pension_porcentage: float, smmlv: float):
    pension_porcentage = pension_porcentage/100
    tasa_remplazo = pension_porcentage-((0.5/100)*(ibl/smmlv))
    return ibl*tasa_remplazo