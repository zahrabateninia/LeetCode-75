#!/usr/bin/env python3
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
i = 0
newStr = ''
if not str1[0] == str2[0]:
    print("")
else:
    for letter in str1:
        if (i < len(str2)):
            if letter == str2[i]:
                i += 1
        else:
            newStr = str1[i:]
    print(newStr)