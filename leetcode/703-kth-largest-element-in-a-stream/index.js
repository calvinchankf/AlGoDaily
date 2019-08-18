/**
 * @param {number} k
 * @param {number[]} nums
 * 
 *  2nd approach: binary search

    Time of init()      O(nlogn)
    Time of add()       O(k)
    Space               O(k)
    184 ms, faster than 57.68%
 */
var KthLargest = function (k, nums) {
    nums.sort((a, b) => a - b)
    if (nums.length > k) {
        nums = nums.slice(nums.length - k)
    }
    this.k = k
    this.nums = nums
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function (val) {
    const idx = bsearch(this.nums, val)
    this.nums.splice(idx, 0, val)
    if (this.nums.length > this.k) {
        this.nums.shift()
    }
    return this.nums[0]
};

const bsearch = function (nums, target) {
    let left = 0
    let right = nums.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target >= nums[mid]) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */