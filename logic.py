# Name: Joshua Smith
# Section: 07

# Purpose: Determine if integer is odd
# Signature: int -> bool
def is_odd(num):
   return num % 2 == 1


# Purpose: Determine if number lies in any of
#          five given intervals
# Signature: float -> bool
def in_an_interval(num):
   # intervals = [
   #    (lambda x: x >= -10, lambda x: x < -4),
   #    (lambda x: x >= -2, lambda x: x <= 8),
   #    (lambda x: x > 27, lambda x: x < 52),
   #    (lambda x: x > 10, lambda x: x <= 22),
   #    (lambda x: x >= 110, lambda x: x <= 237)
   # ]

   # return any([all([check(num) for check in checks]) for checks in intervals])
   return num >= -10 and num < -4 or \
          num >= -2 and num <= 8 or \
          num > 27 and num < 52 or \
          num > 10 and num <= 22 or \
          num >= 110 and num <= 237


# Purpose: Determine if first number is divisible
#          by second number and that both numbers
#          lie whithin a given range.
def is_divisible_in_interval(first, second):
   return (first % second == 0) and \
          (first >= 75 and first <= 140) and \
          (second > 30 and second <= 200)

