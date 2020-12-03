/*
    Time	O(logn) if no duplicates, O(n) if duplicates present on both ends
	Space	O(1)
	76 ms, faster than 94.14%
*/
var search = function(nums, target) {
    let left = 0
    let right = nums.length - 1
    while (left <= right) {
        
        while (left + 1 < right && nums[left] == nums[left+1]) {
            left += 1
        }
        while (left < right-1 && nums[right-1] == nums[right]) {
            right -= 1
        }
        
        const mid = Math.floor((left + right) / 2)
        if (target < nums[mid]) {
            if (nums[left] > nums[mid] || target >= nums[left]) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        } else if (target > nums[mid]) {
            if (nums[mid] > nums[right] || target <= nums[right]) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        } else {
            return true
        }
    }
    return false
};