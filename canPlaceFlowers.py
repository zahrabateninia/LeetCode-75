#!/usr/bin/env python3
"""
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.

"""

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    numOfPlantedFlowers = 0
    i = 0
    while i < len(flowerbed):
        if (
            flowerbed[i] == 0 and
            (i == 0 or flowerbed[i - 1] == 0) and
            (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
        ):
            flowerbed[i] = 1
            numOfPlantedFlowers += 1
        i += 1

    return numOfPlantedFlowers >= n

        
