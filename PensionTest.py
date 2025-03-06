import unittest
from PensionCalculateLogic import calculate_pension
from ErrorPension import *


class CalculaPensiontest(unittest.TestCase):
    def test_normal_1(self):
        base_settlement_income = 3_000_000
        current_legal_minimum_wage = 1_423_500
        pension_porcentage = 65

        expeted_pension = 1_918_387.777

        result = calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)

        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_normal_2(self):
        base_settlement_income = 4_000_000
        current_legal_minimum_wage = 1_300_000
        pension_porcentage = 85

        expeted_pension = 3_338_461.54

        result = calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)

        self.assertAlmostEqual(result, expeted_pension, 2)
    
    def test_normal_3(self):
        base_settlement_income = 5000000
        current_legal_minimum_wage = 1150000
        pension_porcentage = 75.5

        expeted_pension = 3666304.35

        result = calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)
        
        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_exepcional_1(self):
        base_settlement_income = 10_000
        current_legal_minimum_wage = 1_423_500
        pension_porcentage = 20

        expeted_pension = 1_999.65

        result = calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)
        
        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_exepcional_2(self):
        base_settlement_income = 1_300_000
        current_legal_minimum_wage = 1_650_000
        pension_porcentage = 100

        expeted_pension = 1_294_878.79

        result = calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)
        
        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_exepcional_3(self):
        base_settlement_income = 700_000
        current_legal_minimum_wage = 87_000
        pension_porcentage = 65.5

        expeted_pension = 430_339.08

        result = calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)
        
        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_exepcional_4(self):
        base_settlement_income = 25_000_000
        current_legal_minimum_wage = 1_423_500
        pension_porcentage = 99.9

        expeted_pension = 22_779_706.71

        result = calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)

        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_error_1(self):
        base_settlement_income = 0
        current_legal_minimum_wage = 1_250_400
        pension_porcentage = 60.4

        with self.assertRaises(ErrorBaseSettlementIncomeNegative):
            calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)

    def test_error_2(self):
        base_settlement_income = "tres millones quinientos"
        current_legal_minimum_wage = 1_500_000
        pension_porcentage = 6.5

        with self.assertRaises(ErrorBaseSettlementIncomeLetras):
            calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)
    
    def test_error_3(self):
        base_settlement_income = 2_550_450
        current_legal_minimum_wage = 1_360_000
        pension_porcentage = 0

        with self.assertRaises(ErrorPensionPorcentageNegative):
            calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage) 
    
    def test_error_4(self):
        base_settlement_income = 1_250_000
        current_legal_minimum_wage = "un millon docientos"
        pension_porcentage = 35.6

        with self.assertRaises(ErrorCurrentLegalMinimumWageLetras):
            calculate_pension(base_settlement_income, pension_porcentage, current_legal_minimum_wage)

    def test_error_5(self):
        base_settlement_income = 1_720_000
        current_legal_minimum_wage = 0
        pension_poncentage = 24.5

        with self.assertRaises(ErrorCurrentLegalMinimumWageNegative):
            calculate_pension(base_settlement_income, pension_poncentage, current_legal_minimum_wage)



if __name__ == "__main__":
    unittest.main()