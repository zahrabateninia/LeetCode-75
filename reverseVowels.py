"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both 
lower and upper cases, more than once.
"""
s = "leetcOde"
markedVowels = ''
vowels = ['a','e','o','u','i']
newS = ''
vowelsOfS= []
i = 0

for letter in s.lower():
    for vowel in vowels:
        if vowel == letter:
            vowelsOfS.append(letter)
            letter = '0'
    markedVowels += letter
# imp: The reverse() method doesn't return any value. It updates the existing list.
reverseVowels = vowelsOfS.copy()
reverseVowels.reverse()

for letter in markedVowels:
    if letter == '0':
        letter = reverseVowels[i]
        i +=1
    newS += letter
print(newS)



