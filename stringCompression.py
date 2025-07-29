"""
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths that
are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.
"""
# Given array
chars = ['a', 'a', 'b', 'b', 'c']

# Initialize a list to store characters and their counts
compressed_list = []

# Initialize count to keep track of consecutive occurrences
count = 1

# Iterate through the characters starting from the second one
for i in range(1, len(chars)):
    if chars[i] == chars[i-1]:
        count += 1
    else:
        # If the character changes, add the previous character and its count to the list
        compressed_list.append([chars[i-1], count])
        count = 1

# Add the last character and its count to the list
compressed_list.append([chars[-1], count]) 

# Initialize an index to update the original 'chars' array
i = 0

# Iterate through the compressed_list to update 'chars'
for char, occurrence in compressed_list:
    chars[i] = char
    i += 1
    if occurrence > 1:
        for digit in str(occurrence):
            chars[i] = digit
            i += 1

# 'i' now holds the new length of the 'chars' array
print(i)
