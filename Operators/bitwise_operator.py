"""
Bitwise Oeprator => & (and) , | (or) , ^ (XOR) , ~ (not / complement)
                    << (left shift) , >> (right shift)                
                     
"""
a, b = 5, 4
# 4 = 0100 and 5 = 0101
print(a & b)    # 4
print(a | b)    # 1
print(a ^ b)    # 1 (both bits are same then returns 0 otherwise 1)

#  ~ (Not / Complement) : Inverts all the bits. (~x) = -(x+1)
print(~a)       # -6

# << (left shift) : Shifts the bits of a number to the left and Fills the rightmost bits with 0.
#  x << n = x * 2^n

print(a << 2)   # Shift left by 2 positions(bits) -> 010100 = 20

# >> (right shift) : Shifts the bits of a number to the right and Fills the leftmost bits with  0.
# x >> n = x / 2^n

print(a >> 1)    # Shift right by 1 position -> 0010 = 2
