"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both 
lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        markedVowels = ''
        newS = ''
        vowelsOfS= []
        i = 0

        for letter in s:
            if letter == 'a' or letter == 'o' or letter == 'e' or letter == 'u' or letter == 'i' or letter == 'A'or letter == 'E'or letter == 'U'or letter == 'I'or letter == 'O':
                
                    vowelsOfS.append(letter)
                    letter = '|'
            markedVowels += letter
        # imp: The reverse() method doesn't return any value. It updates the existing list.
        reverseVowels = vowelsOfS.copy()
        reverseVowels.reverse()

        for letter in markedVowels:
            if letter == '|':
                letter = reverseVowels[i]
                i +=1
            newS += letter
        return(newS)

