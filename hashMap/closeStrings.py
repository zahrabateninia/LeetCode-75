# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

    
def countOccurrenceOfLetters(word):
    occurrenceOfLetters = {}
    for letter in word:
        if letter in occurrenceOfLetters:
            occurrenceOfLetters[letter] += 1
        else:
            occurrenceOfLetters[letter] = 1
    return occurrenceOfLetters

def closeStrings(word1: str, word2: str) -> bool:
    # if their lengths aren't the same return false
    if len(word1) != len(word2):
         return False

    freqWord1Dict = countOccurrenceOfLetters(word1)
    freqWord2Dict = countOccurrenceOfLetters(word2)

    return set(freqWord1Dict) == set(freqWord2Dict) and sorted(freqWord1Dict.values()) == sorted(freqWord2Dict.values())

  



