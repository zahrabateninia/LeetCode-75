//   Given an array of integers, return indices of the two numbers such that they add up to a specific target.
//   You may assume that each input would have exactly one solution, and you may not use the same element twice.

//   If the array is unsorted:
//  use Brute force using nested loops

const unsortedNrs = [4,2,6,3,1,5,9,7,8,10]
const sortedNrs = [1,2,3,4,5,6,7,8,9,10]

const twoSumUsingTwoPointers = (sortedNums, target) => {
  let left = 0;
  let right = sortedNums.length - 1;
  
  while (left < right) {
    let sum = sortedNums[left] + sortedNums[right];
    
    if (sum === target) {
      return [left, right];
    } else if (sum < target) {
      left++;
    } else {
      right--;
    }
  }
}

twoSumUsingTwoPointers(sortedNrs, 7)
// OUTPUT => [0, 5]