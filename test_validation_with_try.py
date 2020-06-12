"""
Program: test_validation_with_try.py
Author:  Ondrea Li
Date: 6/10/20

The purpose of this program is to test validation_with_try.py
"""

import unittest
import unittest.mock as mock
from Topic4 import validation_with_try as vwt

class MyTestCase(unittest.TestCase):
#my class definitions
    def test_average(self):
         with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert vwt.average(85,90,95) == 90

    def test_average_exception(self):
         with self.assertRaises(ValueError):
             vwt.average(-90, 89, 78)


if __name__ == '__main__':
    unittest.main()




