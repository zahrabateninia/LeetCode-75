# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

def uniqueOccurrences(arr) -> bool:
    # Convert arr to a set
    uniqueMembers = set(arr)
    uniqueOccur = {}

    for member in uniqueMembers:
        memberFreq = arr.count(member)
        # Create a frequency dict
        uniqueOccur[member] = memberFreq
    return (len(set(uniqueOccur.values())) == len(uniqueMembers))




# arr = [1,2,2,1,1,3]
# uniqueMembers = {1,2,3}