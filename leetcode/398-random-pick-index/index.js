/*
    2nd: Reservoir Sampling

    Time of init()  O(1)
    Time of pick()  O(N)
    Space           O(N)
    124 ms, faster than 93.78%
*/
var Solution = function(nums) {
    this.nums = nums
};

/** 
 * @param {number} target
 * @return {number}
 */
Solution.prototype.pick = function(target) {
    let count = 0
    let res = -1
    for (let i = 0; i < this.nums.length; i++) {
        const x = this.nums[i]
        if (x == target) {
            count += 1
            const r = Math.floor(Math.random() * count) + 1
            if (r == 1) {
                res = i
            }
        }
    }
    return res
};