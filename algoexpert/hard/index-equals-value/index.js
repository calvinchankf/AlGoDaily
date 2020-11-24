/*
    binary search
*/
function indexEqualsValue(nums) {
    const n = nums.length
    let left = 0
    let right = n
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (mid <= nums[mid]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    if (left != nums[left]) {
        return -1
    }
    return left
}
// Do not edit the line below.
exports.indexEqualsValue = indexEqualsValue;
  