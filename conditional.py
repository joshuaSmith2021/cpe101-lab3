# Name: Joshua Smith
# Section: 07

# Purpose: Determine smaller of two numbers
# Signature: float float -> float
def min_of_2(first, second):
   return first if first < second else second


# Purpose: Determine smallest of three numbers
# Signature: float float float -> float
def min_of_3(first, second, third):
   first_second_min = min_of_2(first, second)
   return min_of_2(first_second_min, third)


# Purpose: Determine late fee based on days late
# Signature: int -> int
def rental_late_fee(days):
   if days <= 2:
      return 0
   elif days <= 5:
      return 10
   elif days <= 12:
      return 15
   elif days <= 22:
      return 30
   else:
      return 100

