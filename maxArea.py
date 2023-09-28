"""
You are given an integer array height of length n. There are n vertical 
lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""
height = [1,8,6,2,5,4,8,3,7]
def maxArea(height) -> int:
            max_area = 0
            n = len(height)
            
            for i in range(n):
               fixed_side_ptr = height[i]
                
               for j in range(i+1, n):
                     current_side_ptr = height[j]
                    
                     # Smaller number should be considered as height:
                     h = min(fixed_side_ptr, current_side_ptr)
                     w = j - i
                    
                     area = h * w
                    
                     max_area = max(max_area, area)
            
            return max_area

print(maxArea(height))