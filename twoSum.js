//   Given an array of integers, return indices of the two numbers such that they add up to a specific target.
//   You may assume that each input would have exactly one solution, and you may not use the same element twice.

//   If the array is unsorted:
//  use Brute force using nested loops

const unsortedNrs = [4,2,6,3,1,5,9,7,8,10]

const twoSumBrute = (list, target) => {
  for (let i = 0; i < list.length; i++) {
    for (let j = 0; j < list.length; j++) {
      if (list[i] + list[j] === target) {
          return [i, j]
      }
    }
  }
}

twoSumBrute(unsortedNrs, 7)
// OUTPUT => [0, 3]