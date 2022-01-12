
# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Joshua Smith
# Section: 07

import unittest
from logic import *
from logic import in_an_interval
from logic import is_odd

#You can dlete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_is_odd (self):
      # Testing is_odd which checks if a number is odd
      self.assertTrue(is_odd(3))
      self.assertFalse(is_odd(0))
      self.assertTrue(is_odd(-27))
      self.assertFalse(is_odd(-190))
      self.assertFalse(is_odd(100))

   def test_in_an_interval(self):
      # Testing in_an_interval which checks if
      # a number lies in any of five given intervals

      # Given tests
      self.assertFalse(in_an_interval(-12))
      self.assertTrue(in_an_interval(-1))
      self.assertFalse(in_an_interval(9))
      self.assertTrue(in_an_interval(34))
      self.assertFalse(in_an_interval(52))
      self.assertTrue(in_an_interval(147))

      # Custom tests
      self.assertTrue(in_an_interval(-10))
      self.assertFalse(in_an_interval(-4))
      self.assertTrue(in_an_interval(-2))
      self.assertTrue(in_an_interval(8))
      self.assertFalse(in_an_interval(27))
      self.assertTrue(in_an_interval(30))
      self.assertFalse(in_an_interval(10))
      self.assertTrue(in_an_interval(22))
      self.assertTrue(in_an_interval(110))
      self.assertTrue(in_an_interval(237))
      self.assertFalse(in_an_interval(1240))


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

