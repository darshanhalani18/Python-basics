a = input("Enter the value of a = ")
b = input("Enter the value of b = ")

# Display initial values..
print("The initial value of a : "+a)
print("The initial value of b : "+b)
print()

# Swap the values using a temporary variable..
temp = a
a = b
b = temp

#  Display Swapped values..
print("The Swapped value of a :", a)
print("The Swapped value of b :", b)


# Another way to swap numbers..

a = input("a = ")
b = input("b = ")

a, b = b, a

print("a = ", a)
print("b = ", b)
