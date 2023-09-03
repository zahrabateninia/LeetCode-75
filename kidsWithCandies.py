""" 
There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, 
denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, 
after giving the ith kid all the extraCandies, they will have the greatest 
number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""
candies = [2,3,5,1,3]
extraCandies = 3
i = 0
result = []

for kid in candies:
    withExtraCandies = candies[i] + extraCandies  
    if withExtraCandies < max(candies):
        result += [False]
    else:
        result += [True]
    i += 1
print(result)