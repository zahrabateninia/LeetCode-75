"""
Given an integer n, return the decimal value of the binary string formed by 
concatenating the binary representations of 1 to n in order, modulo 109 + 7.
# """
def concatenatedBinary(n: int) -> int:
        return int("".join([bin(i)[2:] for i in range(1,n+1)]),2)%(10**9+7)

print(concatenatedBinary(3))