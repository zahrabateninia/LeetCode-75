//   Given an array of integers, return indices of the two numbers such that they add up to a specific target.
//   You may assume that each input would have exactly one solution, and you may not use the same element twice.

//   If the array is unsorted:
//  use Brute force using nested loops

const unsortedNrs = [4,2,6,3,1,5,9,7,8,10]

const twoSumHashmap = (list, target) => {
  const lookupTable = {}
  
  // build a lookup table
  for (let i = 0; i < list.length; i++) {
    lookupTable[list[i]] = i;
  }
  
  // iterate
  for (let j = 0; j < list.length; j++) {
    let diff = target - list[j]
    if (lookupTable[diff] && lookupTable[diff] !== j) {
      return [j, lookupTable[diff]]
    }
  }
}

twoSumHashmap(unsortedNrs, 7)
// OUTPUT => [0, 3]