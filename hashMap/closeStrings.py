from collections import Counter

# The Counter class is used in your code to count the occurrences of characters in the given words
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return len(word1) == len(word2) \
            and set(word1) == set(word2) \
            and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

