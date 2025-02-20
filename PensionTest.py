import unittest
from PensionCalculateLogic import calculate_pension

class CalculaPensiontest(unittest.TestCase):
    def test_normal_1(self):
        ibl = 3_000_000
        smmlv = 1_423_500
        pension_porcentage = 65

        expeted_pension = 1_918_387.777

        result = calculate_pension(ibl, pension_porcentage, smmlv)

        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_normal_2(self):
        ibl = 4_000_000
        smmlv = 1_300_000
        pension_porcentage = 85

        expeted_pension = 3_338_461.54

        result = calculate_pension(ibl, pension_porcentage, smmlv)

        self.assertAlmostEqual(result, expeted_pension, 2)
    
    def test_normal_3(self):
        ibl = 5000000
        smmlv = 1150000
        pension_porcentage = 75.5

        expeted_pension = 3666304.35

        result = calculate_pension(ibl, pension_porcentage, smmlv)
        
        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_exepcional_1(self):
        ibl = 10000000
        smmlv = 1423500
        pension_porcentage = 20

        expeted_pension = 1648753.07

        result = calculate_pension(ibl, pension_porcentage, smmlv)
        
        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_exepcional_2(self):
        ibl = 1300000
        smmlv = 1650000
        pension_porcentage = 180

        expeted_pension = 2334878.79

        result = calculate_pension(ibl, pension_porcentage, smmlv)
        
        self.assertAlmostEqual(result, expeted_pension, 2)
    
    def test_exepcional_3(self):
        ibl = 700000
        smmlv = 87000
        pension_porcentage = 65.5

        expeted_pension = 430339.08

        result = calculate_pension(ibl, pension_porcentage, smmlv)
        
        self.assertAlmostEqual(result, expeted_pension, 2)

if __name__ == "__main__":
    unittest.main()