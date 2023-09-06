"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both 
lower and upper cases, more than once.
"""
s = "0p"
markedVowels = ''
vowels = ['a','e','o','u','i']
newS = ''
vowelsOfS= []
i = 0

for letter in s:
    for vowel in vowels:
        if vowel == letter or vowel.upper() == letter:
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
print(newS)



