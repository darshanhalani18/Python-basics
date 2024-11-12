"""
Basically Two Membership Operator :
1) in , 2) not in

Membership Operators are used to check whether a character or a
substring or a value or a variable is present in a sequence of characters
(string,list,...)

in - It returns True if specified value is present in a sequence(object) otherwise returns
False.

"""

str = 'Darshan'
print('s' in str)       # True
print('Ds' in str)      # False
print(' ' in str)       # False
print('sa' not in str)  # True

l = [1, 2, 3, -4, 0]
print(0 in l)           # True
print(1 not in l)       # False
