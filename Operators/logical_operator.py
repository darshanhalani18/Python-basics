# Three Logical Operators -> logical and , or , not.

a, b = 5, 10
print(a > 4 and b < 10)     # False
print(a == 5 and b > 5)     # True

print(a == 5 or b < 10)     # True
print(a != 5 or b > 10)     # False

c, d = False, 0
print(not (c))               # True
print(not (d))               # True(1)
