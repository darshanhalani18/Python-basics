"""
Basically two Identity Operator :
1) is , 2) is not

The memory manager in python reuse the objects insted of creating
new objects for the same data with same data type.

So Identity Operator is comparing autually the memory address or Object ID.

and Identity Opearor is working different from equality operator (==)
because eqality operator compares the values not memory address.

"""

a, b = 5, 5
print(a is b)   # True

# In python to check memory address or Object Id

print(id(a), id(b))     # same memory address = 140705906811944

'''
Memory location (address) of both the object a and b are same means autually
both are same object that's why returns True.

print(a is b) is equal to print(id(a) == id(b)) = True
'''
print(a is not b)   # False
print(a == b)       # True

c, d = 5, 5.0           # different data types
print(id(c), id(d))     # 140705906811944 , 1483799376304
print(c is d)           # False- memory address is not same.
print(c is not d)       # True - both objects c and d are not same.

x = 5
print(id(x))    # 140705906811944
x = 6
print(id(x))    # 140705906811976
print(x is x)   # True

"""
here value of x becomes 6 at the end and the address(ID) is changed but since we are checking the ID of the same variable(x = 6), then answer would be True.

"""
