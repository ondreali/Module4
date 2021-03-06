"""
Program: test_coupon_calculations.py
Author:  Ondrea Li
Date: 6/10/20
This program is to Start with your tests, write all combinations you can think of.
You will have multiple tests for each of the ranges.
Write the first test set, commit to github with failing tests
"""
import unittest
from Topic3.Store import coupon_calculation as cc

class MyTestCase(unittest.TestCase):
    #def calculate_price(price, cash_coupon, percent_coupon)
    def test_price_under_10(self):
        value_under_ten = 7.99
        shipping = 5.95
        self.assertAlmostEqual(cc.end_total(value_under_ten, 5, 10, shipping,), 9.16, places=2)
        self.assertAlmostEqual(cc.end_total(value_under_ten, 5, 15, shipping,), 9, places=2)
        self.assertAlmostEqual(cc.end_total(value_under_ten, 5, 20, shipping,), 8.84, places=2)

    def test_price_under_between_ten_thirty(self):
        value_under_thirty = 27.99
        shipping = 7.95
        self.assertAlmostEqual(cc.end_total(value_under_thirty, 5, 10, shipping,), 30.36 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_thirty, 5, 15, shipping,), 29.14 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_thirty, 5, 20, shipping,), 27.92 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_thirty, 10, 10, shipping,), 25.59 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_thirty, 10, 15, shipping,), 24.64 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_thirty, 10, 20, shipping,), 23.68 , places=2)
    def test_price_under_between_thirty_fifty(self):
        value_under_fifty = 49.99
        shipping = 11.95
        self.assertAlmostEqual(cc.end_total(value_under_fifty, 5, 10, shipping,), 55.59 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_fifty, 5, 15, shipping,), 53.20 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_fifty, 5, 20, shipping,), 50.82 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_fifty, 10, 10, shipping,), 50.82 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_fifty, 10, 15, shipping,), 48.70 , places=2)
        self.assertAlmostEqual(cc.end_total(value_under_fifty, 10, 20, shipping,), 46.58 , places=2)
    def test_price_under_over_fifty(self):
        value_over_fifty = 52.99
        shipping = 0
        self.assertAlmostEqual(cc.end_total(value_over_fifty, 5, 10, shipping,), 45.78, places=2)
        self.assertAlmostEqual(cc.end_total(value_over_fifty, 5, 15, shipping,), 43.24 , places=2)
        self.assertAlmostEqual(cc.end_total(value_over_fifty, 5, 20, shipping,), 40.70 , places=2)
        self.assertAlmostEqual(cc.end_total(value_over_fifty, 10, 10, shipping,), 41.01 , places=2)
        self.assertAlmostEqual(cc.end_total(value_over_fifty, 10, 15, shipping,),38.73 , places=2)
        self.assertAlmostEqual(cc.end_total(value_over_fifty, 10, 20, shipping,), 36.46 , places=2)
if __name__ == '__main__':
    unittest.main()
