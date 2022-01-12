# Name: Joshua Smith
# Section: 07

# Purpose: Determine if integer is odd
# Signature: int -> bool
def is_odd(num):
   return num % 2 == 1


# Purpose: Determine if number lies in any of
#          5 given intervals
# Signature: float -> bool
def in_an_interval(num):
   intervals = [
      (lambda x: x >= -10, lambda x: x < -4),
      (lambda x: x >= -2, lambda x: x <= 8),
      (lambda x: x > 27, lambda x: x < 52),
      (lambda x: x > 10, lambda x: x <= 22),
      (lambda x: x >= 110, lambda x: x <= 237)
   ]

   return any([all([check(num) for check in checks]) for checks in intervals])

