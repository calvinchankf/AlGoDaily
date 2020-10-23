/*
    1st approach:
    - store an extra array after rotation
    - put the numbers back to the input

    Time    O(4n)
    Space   O(n)
    84 ms, faster than 86.06%
*/
var rotate = function(nums, k) {
    const n = nums.length
    k = k%n
    const a = nums.slice(0, n-k)
    const b = nums.slice(n-k)
    const c = b.concat(a)
    for (let i = 0; i < n; i++) {
        nums[i] = c[i]
    }
};

/*
    2nd approach: reverse the array

    e.g. [1,2,3,4,5,6,7], k=3

    reverse the whole
    [7,6,5,4,3,2,1]

    reverse the k front items
    [5,6,7,4,3,2,1]

    reverse the 2nd half
    [5,6,7,1,2,3,4]

    Time    O(3n)
    Space   O(1)
    92 ms, faster than 66.98%
*/
var rotate = function(nums, k) {
    const n = nums.length
    k = k%n
    reverseSubArray(nums, 0, n-1)
    reverseSubArray(nums, 0, k-1)
    reverseSubArray(nums, k, n-1)
};

const reverseSubArray = (nums, i, j) => {
    while (i < j) {
        const temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1
    }
}