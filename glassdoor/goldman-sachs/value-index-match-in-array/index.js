/*
    https://www.glassdoor.com.hk/Interview/Goldman-Sachs-Front-End-Engineer-Interview-Questions-EI_IE2800.0,13_KO14,32.htm?countryRedirect=true

    Given an array of unique sorted numbers.
    Find out if there is an array's value that matches its index.
*/
const findValueIndexMatch = (nums) => {
    let left = 0
    let right = nums.length-1
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (nums[mid] == mid) {
            return mid
        } else if (nums[mid] < mid) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}

// -1 not found
console.log(findValueIndexMatch([1, 2, 4, 6, 8, 10]))

// 0
console.log(findValueIndexMatch([0, 2, 4, 6, 8, 10]))

// 1
console.log(findValueIndexMatch([-10, 1, 4, 6, 8, 10]))

// 2
console.log(findValueIndexMatch([-10, -8, 2 ,6, 8, 10]))

// 3
console.log(findValueIndexMatch([-10, -8, -6 ,3, 8, 10]))

// 4
console.log(findValueIndexMatch([-10, -8, -6 ,-4, 4, 10]))

// 5
console.log(findValueIndexMatch([-10, -8, -6 ,-4, -2, 5]))

console.log("----")

/*
    followup: search the range of all the matches
*/
const findValueIndexMatches = (nums) => {
    const left = lowerBsearch(nums)
    const right = upperBsearch(nums) - 1
    if (nums[left] != left || nums[right != right]) {
        return []
    }
    return [left, right]
}

const lowerBsearch = (nums) => {
    let left = 0
    let right = nums.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (mid <= nums[mid]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}

const upperBsearch = (nums) => {
    let left = 0
    let right = nums.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (mid >= nums[mid]) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}

// -1 not found
console.log(findValueIndexMatches([1, 2, 4, 6, 8, 10]))

// [0, 0]
console.log(findValueIndexMatches([0, 2, 4, 6, 8, 10]))

// [1, 1]
console.log(findValueIndexMatches([-10, 1, 4, 6, 8, 10]))

// [2, 2]
console.log(findValueIndexMatches([-10, -8, 2 ,6, 8, 10]))

// [3, 3]
console.log(findValueIndexMatches([-10, -8, -6 ,3, 8, 10]))

// [4, 4]
console.log(findValueIndexMatches([-10, -8, -6 ,-4, 4, 10]))

// [5, 5]
console.log(findValueIndexMatches([-10, -8, -6 ,-4, -2, 5]))

console.log("-----")

// [0, 1]
console.log(findValueIndexMatches([0, 1, 4, 6, 8, 10]))

// [1, 2]
console.log(findValueIndexMatches([-10, 1, 2, 6, 8, 10]))

// [1, 3]
console.log(findValueIndexMatches([-10, 1, 2 ,3, 8, 10]))

// [1, 4]
console.log(findValueIndexMatches([-10, 1, 2 ,3, 4, 10]))

// [4, 5]
console.log(findValueIndexMatches([-10, -8, -6 ,-4, 4, 5]))

// [0, 5]
console.log(findValueIndexMatches([0, 1, 2, 3, 4, 5]))

