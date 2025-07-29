"""
You are given two strings word1 and word2. Merge the strings by adding letters in 
alternating order, starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.
Return the merged string.
"""
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

def merge(word1, word2):
    result = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
    return ''.join(result) # concatenate the characters from the result list into a single string

merged_string = merge(word1,word2) 
print(merged_string)