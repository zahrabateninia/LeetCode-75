"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

"""
import re

s = "the sky is   blue"
words = re.findall(r"\w*", s)  # ['the', '', 'sky', '', 'is', '', '', '', 'blue', '']
noSpaceWords = []
for word in words:
    if word == "":
        continue
    noSpaceWords.append(word)

noSpaceWords.reverse()
print(" ".join(noSpaceWords))
