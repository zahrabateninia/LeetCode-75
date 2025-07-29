"""
You are given an integer array height of length n. There are n vertical 
lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""
def maxArea(height) -> int:
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        area = h * w
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = maxArea(height)
print(result)
