"""
Given an integer n, return the decimal value of the binary string formed by 
concatenating the binary representations of 1 to n in order, modulo 109 + 7.
"""
n=75
remainders = []
while n > 0:
    d = n//2
    r = n % 2
    remainders.append(str(r))
    n = d
remainders.reverse()
strRemainders = ''.join(remainders) # convert the list to string

print(strRemainders)