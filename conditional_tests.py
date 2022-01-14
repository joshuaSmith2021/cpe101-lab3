# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Joshua Smith
# Section: 07

import unittest
from math import e, pi
from conditional import *
from conditional import min_of_2
from conditional import min_of_3

#You can delete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_min_of_2(self):
      # Testing min_of_2 which determines smaller of two numbers
      self.assertEqual(min_of_2(4, 6), 4)
      self.assertEqual(min_of_2(-12, -24), -24)
      self.assertAlmostEqual(min_of_2(e * pi, 60), 8.53973422267)
      self.assertEqual(min_of_2(0, 0), 0)

   def test_min_of_3(self):
      # Testing min_of_3 which determines smallest of three numbers
      self.assertEqual(min_of_3(0, 3, 6), 0)
      self.assertEqual(min_of_3(-124, 325, -124978), -124978),
      self.assertEqual(min_of_3(0, 1, 0), 0)
      self.assertEqual(min_of_3(-1, 0, 0), -1)
      self.assertEqual(min_of_3(pi * e, 0, 14), 0)
      self.assertAlmostEqual(min_of_3(0, 0, 0), 0)

   def test_rental_late_fee(self):
      # Testing rental_late_fee which determines late fee based on days late
      self.assertEqual(rental_late_fee(0), 0)
      self.assertEqual(rental_late_fee(2), 0)
      self.assertEqual(rental_late_fee(3), 10)
      self.assertEqual(rental_late_fee(5), 10)
      self.assertEqual(rental_late_fee(6), 15)
      self.assertEqual(rental_late_fee(12), 15)
      self.assertEqual(rental_late_fee(13), 30)
      self.assertEqual(rental_late_fee(22), 30)
      self.assertEqual(rental_late_fee(23), 100)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

