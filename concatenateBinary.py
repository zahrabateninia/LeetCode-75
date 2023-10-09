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
num = 1001011
listNum = [int(x) for x in str(num)]
sqr = 0
decimal = 0
listNum.reverse()
for digit in listNum:
    if digit == 1:
        digit = 2**sqr
        decimal += digit
    
    sqr += 1
print(decimal)
        
