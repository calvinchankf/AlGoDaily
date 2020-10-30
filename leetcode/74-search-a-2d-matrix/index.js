/*
    1st approach:
	- upper bound binary search to look for the target range
	- binary search to look for the item within that range
    
	Time 	O(RlogC)
	Space   O(1)
	64 ms, faster than 99.14%
*/
var searchMatrix = function(matrix, target) {
    for (let i = 0; i < matrix.length; i++) {
        const nums = matrix[i]
        const j = bsearch(nums, target)
        if (j >= 0 && j < nums.length) {
            return true
        }
    }
    return false
};

const bsearch = (nums, target) => {
    let left = 0
    let right = nums.length -1
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (target < nums[mid]) {
            right = mid - 1
        } else if (target > nums[mid]) {
            left = mid + 1
        } else {
            return mid
        }
    }
    return -1
}

/*
    2nd approach:
	- lower bound binary search to look for the target range
    - binary search to look for the item within that range
    
	Time 	O(logR + logC)
	Space   O(1)
	84 ms, faster than 35.77%
*/
var searchMatrix = function(matrix, target) {
    if (matrix.length == 0 || matrix[0].length == 0) {
        return false
    }
    const R = matrix.length
    const C =  matrix[0].length
    let left = 0
    let right = R
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target <= matrix[mid][C-1]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    if (right < 0 || right == R) {
        return false
    }
    const nums = matrix[right]
    const j = bsearch(nums, target)
    if (j < 0 || j == C) {
        return false
    }
    return true
};

const bsearch = (nums, target) => {
    let left = 0
    let right = nums.length -1
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (target < nums[mid]) {
            right = mid - 1
        } else if (target > nums[mid]) {
            left = mid + 1
        } else {
            return mid
        }
    }
    return -1
}

/*
    3rd approach:
	- upper bound binary search to look for the target range
	- binary search to look for the item within that range
    
	Time 	O(logR + logC)
	Space   O(1)
	64 ms, faster than 99.14%
*/
var searchMatrix = function(matrix, target) {
    if (matrix.length == 0 || matrix[0].length == 0) {
        return false
    }
    const R = matrix.length
    const C =  matrix[0].length
    let left = 0
    let right = R
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target >= matrix[mid][0]) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    if (right-1 < 0) {
        return false
    }
    const nums = matrix[right-1]
    const j = bsearch(nums, target)
    if (j < 0 || j == C) {
        return false
    }
    return true
};

const bsearch = (nums, target) => {
    let left = 0
    let right = nums.length -1
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (target < nums[mid]) {
            right = mid - 1
        } else if (target > nums[mid]) {
            left = mid + 1
        } else {
            return mid
        }
    }
    return -1
}