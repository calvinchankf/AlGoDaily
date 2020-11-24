/*
    similar to lc75
*/
function threeNumberSort(nums, order) {
    // Write your code here.
    const n = nums.length
    const left = order[0]
    const right = order[order.length-1]
    let j = 0
    for (let i = 0; i < n; i++) {
        if (nums[i] == left) {
            [nums[i], nums[j]] = [nums[j], nums[i]]
            j += 1
        }
    }

    j = n - 1
    for (let i = n - 1; i >= 0; i--) {
        if (nums[i] == right) {
            [nums[i], nums[j]] = [nums[j], nums[i]]
            j -= 1
        }
    }
    return nums
  }
  
  // Do not edit the line below.
  exports.threeNumberSort = threeNumberSort;
  