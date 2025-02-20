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
        ibl = 10_000
        smmlv = 1_423_500
        pension_porcentage = 20

        expeted_pension = 1_999.65

        result = calculate_pension(ibl, pension_porcentage, smmlv)
        
        self.assertAlmostEqual(result, expeted_pension, 2)

    def test_exepcional_2(self):
        ibl = 1_300_000
        smmlv = 1_650_000
        pension_porcentage = 100

        expeted_pension = 1_294_878.79

        result = calculate_pension(ibl, pension_porcentage, smmlv)
        
        self.assertAlmostEqual(result, expeted_pension, 2)
    
    def test_exepcional_3(self):
        ibl = 700_000
        smmlv = 87_000
        pension_porcentage = 65.5

        expeted_pension = 430_339.08

        result = calculate_pension(ibl, pension_porcentage, smmlv)
        
        self.assertAlmostEqual(result, expeted_pension, 2)
    
    def test_exepcional_4(self):
        ibl = 25_000_000
        smmlv = 1_423_500
        pension_porcentage = 99.9

        expeted_pension = 22_779_706.71

        result = calculate_pension(ibl, pension_porcentage, smmlv)

        self.assertAlmostEqual(result, expeted_pension, 2)

if __name__ == "__main__":
    unittest.main()