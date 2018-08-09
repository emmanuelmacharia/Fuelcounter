import unittest
from fuel import Fuelcalculator

class Testfuelcounter(unittest.TestCase):
    '''creating a test case for the fuel.py module'''

    def setUp(self):
        self.test = Fuelcalculator('Nissan', 'Xtrail', 10.0, 100.1, 105)
    def tearDown(self):
        pass

    def test_input_numbers(self):
        '''tests whether the input has successfully been converted into a float'''
        self.assertIsInstance(self.test.mpg, float)
        self.assertIsInstance(self.test.distance, float)

    def test_mpg_to_kmplitre(self):
        '''tests the accuracy of the mpg to kmplire converter'''
        self.test.mpg_to_kmplitre()
        self.assertAlmostEqual(self.test.mpg_to_kmplitre(), 4.251436831710789)

    def test_fueluse(self):
        '''tests the accuracy of the fuel use function'''
        fuel_used = self.test.fueluse()
        self.assertEqual(fuel_used, 23.544981135170598)
        #self.assertEqual(self.test.fueluse(100.5,10), 10.05)

    def test_cost(self):
        self.test.cost()
        self.assertEqual(round(self.test.cost(),2), 2472.22)







if __name__ == '__main__':
    unittest.main()