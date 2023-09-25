"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. (i.e., "ace" is a subsequence 
of "abcde" while "aec" is not).
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0  # Pointer for string s
        t_ptr = 0  # Pointer for string t

        while s_ptr < len(s) and t_ptr < len(t):
            # Check if the characters at the pointers match
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1  # Move the pointer for s if there's a match
            t_ptr += 1  # Always move the pointer for t

        return s_ptr == len(s)  # If s_ptr reached the end of s, it's a subsequence
