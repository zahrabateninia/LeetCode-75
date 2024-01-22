# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


def uniqueOccurrences(arr) -> bool:
    # Create a frequency dict in a single pass
    freqDict = {}
    for num in arr:
        if num in freqDict:
            freqDict[num] += 1
        else:
            freqDict[num] = 1

    # Check if the occurrences are unique
    return len(set(freqDict.values())) == len(freqDict.values())
