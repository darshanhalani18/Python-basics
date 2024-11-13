"""
basic Syntax :
round(number you want to round off , no. of digits up to which you want to round off )
second argument is optional..

"""

print(round(20.33))         # 20
print(round(21.655555, 2))  # 21.66
print(round(10.99))         # 11
print(round(5))             # 5
print(round(5, 2))          # 5
print(round(5.9, 0))        # 6.0
print(round(18.556677, 3))  # 18.557

# The tie-breaking rule for the round() function in Python applies to halfway values (0.5).
# When a number ends in 0.5 (e.g. 2.5, 3.5), Python's round() uses "Round Half to Even" (Bankers' Rounding).
# This means that if the decimal is exactly 0.5, it will round to the nearest even integer.

# For example:
#   round(2.5) -> 2 (since 2 is even)
#   round(3.5) -> 4 (since 4 is even)

print(round(15.5))       # 16
print(round(12.5))       # 12

# In Python, when rounding with a negative n digits (e.g., round(674, -1))
# The round function rounds to the nearest 10, 100, 1000, etc..depending on the value of n digits.
# For example, round(674, -1) rounds to the nearest 10 (10^1), resulting in 670.
# This is equivalent to rounding 674 to the nearest 10^(-(-1)) or 10^1.

#   round(674, -1) -> 670 (rounds to the nearest 10)
#   round(674, -2) -> 700 (rounds to the nearest 100)

print(round(674, -1))        # 670
print(round(674, -3))        # 1000
print(round(674.78, -2))     # 700.00
print(round(675, -1))        # 680
print(round(2.67, -1))       # 0.0
print(round(-1.5))           # -2
print(round(-8/3))           # -3
print(round(-83.6, -1))      # -80.0
print(round(467, -4))         # 0
