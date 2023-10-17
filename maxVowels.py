"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
"""
def maxVowels(s: str, k: int) -> int:
    vowels = set('aeiou')
    window = s[:k]
    max_vowels = sum(1 for char in window if char in vowels)
    max_count = max_vowels

    for i in range(k, len(s)):
        if s[i - k] in vowels:
            max_vowels -= 1
        if s[i] in vowels:
            max_vowels += 1
        max_count = max(max_count, max_vowels)

    return max_count

s = 'abciiidef'
k = 3
print(maxVowels(s, k))  # Output: 3
