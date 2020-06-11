"""
Program: test_coupon_calculations.py
Author:  Ondrea Li
Date: 6/10/20
This program tests a function that prints 'Hello World'
as output.  The function is then called.
"""
import unittest
from Module4.Store import Coupon_Calculations as cc

class MyTestCase(unittest.TestCase):
    #def calculate_price(price, cash_coupon, percent_coupon)
    def test_price_under_10(self):
        value_under_ten = 7.99
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 10), 9.16, places=4)
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 15), 9, places=4)
        self.assertAlmostEqual(cc.calculate_price(7.99, 5, 20), 8.84, places=4)
        self.assertAlmostEqual(cc.calculate_price(7.99, 10, 100), 9.48, places=4)

    def test_price_10_to_less_than_30(self):
        value_under_ten = 27.99
        self.assertAlmostEqual(cc.calculate_price(27.99, 5, 10), 29.14, places=4)
        self.assertAlmostEqual(cc.calculate_price(27.99, 5, 15), 25.59, places=4)
        self.assertAlmostEqual(cc.calculate_price(27.99, 5, 20), 24.64, places=4)
        self.assertAlmostEqual(cc.calculate_price(27.99, 10, 100), 23.68, places=4)




if __name__ == '__main__':
    unittest.main()
