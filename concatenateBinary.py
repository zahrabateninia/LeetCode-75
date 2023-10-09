"""
Given an integer n, return the decimal value of the binary string formed by 
concatenating the binary representations of 1 to n in order, modulo 109 + 7.
# """
class Solution:
    def concatenatedBinary(self, n: int) -> int:
            concatenated_binary = ''

            for i in range(1, n+1):
                # Convert i to binary and append to concatenated_binary
                binary_i = bin(i)[2:]  # Removing the '0b' prefix
                concatenated_binary += binary_i

            # Convert binary to decimal
            decimal_value = 0
            for idx, bit in enumerate(reversed(concatenated_binary)):
                if bit == '1':
                    decimal_value += 2 ** idx

            # Calculate modulo 10^9 + 7
            result = decimal_value % (10**9 + 7)
            return result
