#!/usr/bin/env python3
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
def gcdOfStrings(str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return gcdOfStrings(str1[len(str2):], str2) # using recursive function
        return gcdOfStrings(str1, str2[len(str1):])


print(gcdOfStrings(str1,str2))
"""
If str1 is longer than str2, the function recursively calls itself with the substring of str1 
that starts at the length of str2 and the original str2. 
This effectively removes the common prefix of str2 from str1 and 
continues the search for a common divisor in the remaining part of str1.

"""

