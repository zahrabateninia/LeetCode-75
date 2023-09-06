"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both 
lower and upper cases, more than once.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'o', 'i', 'e', 'u', 'A', 'O', 'I', 'E', 'U'}
        l, r = 0, len(s)-1
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l] not in vowels:
                    l += 1
                if s[r] not in vowels:
                    r -= 1
        return ''.join(s)
